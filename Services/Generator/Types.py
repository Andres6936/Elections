from typing import TypeVar, Optional, Sequence

from fastapi import Depends
from pydantic import BaseModel

# Can be any subtype of BaseModel
T = TypeVar("T", bound=BaseModel)

# The typing.Sequence type hint in Python represents an immutable sequence of values. An immutable sequence
# is a sequence that cannot be modified after it is created. Examples of immutable sequences in Python
# include strings, tuples, and frozen sets.

# The typing.Sequence type hint can be used to specify the expected type of variable, function parameter,
# or return value. For example, the following code defines a function that takes a typing.Sequence of integers
# as a parameter and returns the sum of the integers:

# def sum_sequence(sequence: Sequence[int]) -> int:
#    ....
# result = sum_sequence([1, 2, 3, 4, 5])
Dependencies = Optional[Sequence[Depends]]
