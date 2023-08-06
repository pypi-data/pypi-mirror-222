from __future__ import annotations
from enum import Enum
from typing import Callable, TypeVar, Iterable, Optional, Any

T = TypeVar("T")
W = TypeVar("W")

def validated_input(
    msg: str | None = None,
    validators: Iterable[tuple[Callable[[T], bool], str | Callable[[T], str] | None]] | None = None,
    constructor: Callable[[T], W] = str,
    precomp: Callable[[str], T] | None = None,
    precomp_error: str | Callable[[str], str] | None = None
) -> Callable[[], W]:
    """
    An attempt at abstracting the case of using input() repeatedly until it is valid;
    Returns a function (to use instead of input()), but the message is specified at the part of calling this function,
    not the function you get itself, mostly because the error messages in the validator argument should be related to the input message.

    When validators aren't specified, it uses the constructor as the validator. I.e, if you use constructor=int, the validator will check if the input is an integer.

    If an error is raised during the process of validation, it will count as a fail of validation, so 
    you can use this to make easy typechecks by using something like:
    `lambda buffer: float(buffer) or True` as a validator function.

    The precomp(utation) function will be applied to the input before validation `and` when it will be passed to a constructor. [ It applies to the value of input() ]
    """

    if msg is None:
        msg = f"Enter a {constructor}: "

    if validators is None:
        validators = [
            (lambda buffer: constructor(buffer) or True, lambda buffer: f"<{buffer}> is not a valid {constructor}")
        ]
    
    if precomp_error is None:
        precomp_error = "Precomputation failed at input == <{buffer}> :("
        
    def inner() -> W:
        while True:

            buffer: str = input(msg)

            if precomp is not None:
                try:
                    buffer: T = precomp(buffer)
                except:
                    print(precomp_error(buffer) if callable(precomp_error) else precomp_error.format(buffer=buffer))
                    continue

            for validator, err_msg in validators:
                result: bool
                try:
                    result = validator(buffer)
                except:
                    result = False

                if not result:
                    if err_msg is not None:
                        print(err_msg(buffer) if callable(err_msg) else err_msg.format(buffer=buffer))
                    break

            else: # if no break happens in validation checking - return
                return constructor(buffer)
                
    return inner

# --- # 

class Case:
    class _Mode(Enum):
        match = 0 # pass same args, see if output matches
        validate = 1 # pass same args to both, see if kwargs.get("validator") passes

    def __init__(self, function, *_, **kwargs):
        if len(kwargs) == 0: self.mode = Case._Mode.match
        elif len(kwargs) == 1 and ("validator" in kwargs): self.mode = Case._Mode.validate; self.validator = kwargs["validator"]
        else: raise ValueError("Currently a not supported case")
        self.function = function

    def __repr__(self) -> str:
        return f"Case(function = {self.function.__name__}, mode = {self.mode})"

def parametrized(
    expected_io: list[
        (tuple[tuple[Any, ...] | list[Any], Any | Case | Exception]) | 
        (tuple[tuple[Any, ...] | list[Any], dict[str, Any], Any | Case | Exception]) |
        (list[tuple[Any, ...] | list[Any], Any | Case | Exception]) | 
        (list[tuple[Any, ...] | list[Any], dict[str, Any], Any | Case | Exception])
    # problem? :trollface: :union_type: :trollge:
]) -> Callable[[Callable], Callable]: # returns a decorator

    #
    # [
    #   (*args: tuple | list, **kwargs: Optional[dict[str, Any]], expect: Any | Case | Exception),
    #   ...
    # ]
    #

    class _TestMode(Enum):
        normal_case: int = 0
        case_test: int = 1
        exception_test: int = 2

        @classmethod
        def from_expect(cls: _TestMode, expect: Any | Case | Exception) -> _TestMode:
            # Exception test:
            try:
                if isinstance(expect(), Exception): return cls.exception_test
            except:
                if isinstance(expect, Exception): return cls.exception_test

            if isinstance(expect, Case): return cls.case_test

            else: return cls.normal_case


    def parametrized_decorator(function):

        def parse_case(*, args: Optional[tuple[Any, ...] | list[Any]] = (), kwargs: Optional[dict[str, Any]] = {}, expect: Any | Case | Exception) -> None:

            test_mode: _TestMode = _TestMode.from_expect(expect=expect)

            info: str = f"{function.__name__}({repr(args)*bool(args)}{(', '*(bool(args) and bool(kwargs)))+repr(kwargs)*bool(kwargs)})"

            match test_mode:
                case _TestMode.normal_case:
                    # in a normal case, we just call the function with the provided arguments, and check if the result matches expectations
                    try:
                        result = function(*args, **kwargs) if kwargs else function(*args)
                        callable_expect = callable(expect)
                        expectation_passed = expect(result) if callable_expect else expect == result
                        if expectation_passed:
                            print(f"\x1B[38;5;154mTest passed: {info} -> {result} {f'so {expect.__name__}({result}) was truthy' if callable_expect else f'== {expect}'}\x1B[0m")
                        else:
                            print(f"\x1B[38;5;196mTest failed: {info} -> {result} {f'so {expect.__name__}({result}) was falsy' if callable_expect else f'instead of {expect}'}\x1B[0m")
                            
                    except Exception as exc:
                        # something gone wrong, because this is not an exception test, so the test basically "failed"
                        print(f"\x1B[38;5;99mTest raised an exception: {info} -> {repr(exc)}\x1B[0m")
                
                case _TestMode.case_test:

                    buf_info: str = f"{expect.function.__name__}({repr(args)*bool(args)}{(', '*(bool(args) and bool(kwargs)))+repr(kwargs)*bool(kwargs)})"
                    # in a `case test`, we call 2 functions with the same arguments: the one we're decorating, and the one provided in the case instance, BUT the test case itself has multiple modes: match and validate. 

                    # if mode is match, we just compare if the function we're decorating and the function in the case instance give the same arguments
                    # if mode is validate, we get results of both functions, and see if the result of calling case.validator with those results is truthy

                    # in both cases the first function will be needed to be run, so call it before matching the mode & handle the exception:
                    exc_0: Exception | None = None
                    exc_1: Exception | None = None

                    # Gather expections from both functions to indicate the messages
                    try:
                        result_0 = function(*args, **kwargs) if kwargs else function(*args)
                    except Exception as exc_0_buf:
                        exc_0 = exc_0_buf

                    try:
                        result_1 = expect.function(*args, **kwargs) if kwargs else expect.function(*args)
                    except Exception as exc_1_buf:
                        exc_1 = exc_1_buf
                    
                    if exc_0 and exc_1:
                        # Both functions raised an exception
                        print(f"\x1B[38;5;196mCase test failed: both functions raised an exception: {repr(exc_0)} : {repr(exc_1)}\x1B[0m")
                    elif exc_0 and not exc_1:
                        # Only the first (decorated) function raised an exception
                        print(f"\x1B[38;5;196mCase test failed: {function.__name__} raised an exception {repr(exc_0)}\x1B[0m")
                    elif exc_1 and not exc_0:
                        # Only the second (provided in the case instance) function raised an exception
                        print(f"\x1B[38;5;196mCase test failed: {expect.function.__name__} raised an exception {repr(exc_1)}\x1B[0m")
                    
                    if any([exc_0, exc_1]): return None

                    match expect.mode:

                        case Case._Mode.match:

                            if result_0 == result_1:
                                # Match passed
                                print(f"\x1B[38;5;154mMatch case passed: {info} == {buf_info} -> {result_0} | {result_1}\x1B[0m")
                            else:
                                # Match failed
                                print(f"\x1B[38;5;196mMatch case failed: {info} -> {result_0} ; {buf_info} -> {result_1}\x1B[0m")

                        case Case._Mode.validate:
                            
                            buf_res: Any = expect.validator(result_0, result_1)
                            buf_info: str = f"{expect.validator.__name__}({repr(result_0)}, {repr(result_1)})"

                            if buf_res:
                                # Validation passed
                                print(f"\x1B[38;5;154mValidation case passed: {buf_info} -> {buf_res} [is truthy]\x1B[0m")
                            else:
                                # Validation failed
                                print(f"\x1B[38;5;196mValidation case failed: {buf_info} -> {buf_res} [is falsy]\x1B[0m")


                case _TestMode.exception_test:
                    # in an exception test, we call the function with the provided arguments, and see if the catched expection matches the expected one.
                    try:
                        result = function(*args, **kwargs) if kwargs else function(*args)
                        print(f"\x1B[38;5;202mException test didnt result in an exception {info} -> {result} instead of raising {repr(expect())}\x1B[0m")
                    except Exception as exc:
                        if type(exc) == expect:
                            print(f"\x1B[38;5;50mException test passed: {info} -> {repr(exc)}\x1B[0m")
                        else:
                            print(f"\x1B[38;5;196mException test failed: {info} -> {repr(exc)} instead of {repr(expect())}\x1B[0m")

        def test_cases() -> None:
            
            for test_case in expected_io:
                if len(test_case) == 2:
                    if isinstance(test_case[0], dict):
                        parse_case(kwargs=test_case[0], expect=test_case[1])
                    else:
                        parse_case(args=test_case[0], expect=test_case[1])
                elif len(test_case) == 3: parse_case(args=test_case[0], kwargs=test_case[1], expect=test_case[2])

        test_cases()

        return function
    
    return parametrized_decorator