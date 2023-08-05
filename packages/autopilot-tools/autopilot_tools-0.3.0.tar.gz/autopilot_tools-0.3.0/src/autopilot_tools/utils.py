from typing import Callable, TypeVar, Union

T = TypeVar('T')


def retry_command(
        fun: Callable[[], Union[T, None]], times=3,
        test: Callable[[T], bool] = lambda x: x is not None) -> Union[T, None]:
    exc = None
    for _ in range(times):
        try:
            res = fun()
            if test(res):
                return res
            # I'm re-raising it later down the line anyways
        except Exception as e:  # pylint: disable=broad-except
            exc = e
    if exc is not None:
        raise exc
    return None
