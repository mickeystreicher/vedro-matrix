from itertools import product
from typing import Any, Callable

from vedro import params

__version__ = "0.1.0"
__all__ = ("params_matrix", "ParamsMatrix",)


class ParamsMatrix:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._args = args
        self._kwargs = kwargs

    def __call__(self, fn: Callable[..., None]) -> Callable[..., None]:
        iterables = list(self._args) + list(self._kwargs.values())
        combinations = list(product(*iterables))
        for combo in reversed(combinations):
            fn = params(*combo)(fn)
        return fn


params_matrix = ParamsMatrix
