from itertools import product
from typing import Any, Callable, Iterable

from vedro import params

__version__ = "1.0.0"
__all__ = ("params_matrix", "ParamsMatrix",)


class ParamsMatrix:
    """
    A decorator for parameterized testing that generates all combinations of the provided
    test parameters to create multiple test scenarios.

    Parameters:
        *args: Iterable positional arguments representing the test parameters.
        **kwargs: Iterable keyword arguments representing the test parameters.

    Raises:
        ValueError: If no iterable arguments are provided.

    Example usage:
        class Scenario(vedro.Scenario):
            @params_matrix([1, 2], [True, False])
            def __init__(self, post_id, is_deleted):
                ...

    This will generate and run scenarios with the following parameter combinations:
    - Scenario 1: post_id=1, is_deleted=True
    - Scenario 2: post_id=1, is_deleted=False
    - Scenario 3: post_id=2, is_deleted=True
    - Scenario 4: post_id=2, is_deleted=False
    """

    def __init__(self, *args: Iterable[Any], **kwargs: Iterable[Any]) -> None:
        if not args and not kwargs:
            raise ValueError("At least one iterable argument must be provided "
                             "for parameterization")
        self._args = args
        self._kwargs = kwargs

    def __call__(self, fn: Callable[..., None]) -> Callable[..., None]:
        iterables = list(self._args) + list(self._kwargs.values())
        combinations = list(product(*iterables))
        for combo in reversed(combinations):
            fn = params(*combo)(fn)
        return fn


# Alias for easier usage
params_matrix = ParamsMatrix
