# attributes.py

from typing import (
    Self, Iterable, Any, Optional,
    Type, Union, Generic, TypeVar
)
import string
import random
from abc import ABCMeta

from represent import represent, Modifiers

__all__ = [
    "Arguments",
    "Attribute",
    "NumericAttribute",
    "StringAttribute",
    "IntegerAttribute",
    "FloatAttribute"
]

@represent
class Arguments:
    """A class to represent a fitness function."""

    __slots__ = "args", "kwargs"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls the fitness function on the solution.

        :param args: Any positional arguments.
        :param kwargs: Any keyword arguments.
        """

        self.args = args or ()
        self.kwargs = kwargs or {}

        self.update(*args, **kwargs)
    # end __init__

    def update(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls the fitness function on the solution.

        :param args: Any positional arguments.
        :param kwargs: Any keyword arguments.
        """

        self.args = args or self.args
        self.kwargs = kwargs or self.kwargs
    # end update

    def copy(self) -> Self:
        """
        Returns a copy of the definition object.

        :return: The new definition object.
        """

        return Arguments(*self.args, **self.kwargs)
    # end copy
# end Arguments

_V = TypeVar("_V")

@represent
class Attribute(Generic[_V], metaclass=ABCMeta):
    """A class to represent an attribute of a solution."""

    NAME: Optional[str] = None

    EXCLUDED: Iterable[Any] = []

    arguments = Arguments()

    __modifiers__ = Modifiers()
    __modifiers__.properties = True

    __slots__ = "_value", "name"

    def __init__(self, value: _V, name: Optional[str] = None) -> None:
        """
        Defines the class attributes.

        :param value: The value of the attribute.
        :param name: The name of the attribute.
        """

        self.name = name or self.NAME

        self._value: _V = value
    # end __init__

    def __hash__(self) -> int:
        """
        Returns the hash of the object.

        :return: The hash of the object.
        """

        return id(self)
    # end __hash__

    def __eq__(self, other: Self) -> bool:
        """
        Checks if the solutions are equal.

        :param other: The other solution.

        :return: The equality value.
        """

        return (
            (type(self) is type(other)) and
            (self.name == other.name) and
            (self.value == other.value)
        )
    # end __eq__

    @property
    def value(self) -> _V:
        """
        Returns the value of the attribute.

        :return: The value.
        """

        if not isinstance(self._value, Attribute):
            return self._value

        else:
            return self._value.value
        # end if
    # end value

    @classmethod
    def build(cls, *args: Any, **kwargs: Any) -> Self:
        """
        Generates the random attribute.

        :param args: Any positional arguments.
        :param kwargs: Any keyword arguments.

        :return: The attribute object.
        """

        while (value := cls.generate(*args, **kwargs)) in cls.EXCLUDED:
            pass
        # end while

        return cls(value=value)
    # end build

    @classmethod
    def generate(cls, *args: Any, **kwargs: Any) -> _V:
        """
        Generates the random attribute value.

        :param args: Any positional arguments.
        :param kwargs: Any keyword arguments.

        :return: The attribute value.
        """
    # end generate

    def copy(self) -> Self:
        """
        Copies the object.

        :return: A new copy of the object.
        """

        return type(self)(value=self._value, name=self.name)
    # end copy
# end Attribute

Number = Union[int, float]

_NV = TypeVar("_NV", int, float)

class NumericAttribute(Attribute[Number], Generic[_NV]):
    """A class to represent an attribute of a solution."""

    BASE: Type[Number] = float

    FLOOR: Number = None
    ROOF: Number = None
    STEP: Optional[Number] = None
    PRECISION: Optional[Number] = None

    __slots__ = ()

    @classmethod
    def generate(
            cls,
            base: Optional[Type[Number]] = None,
            floor: Optional[Number] = None,
            roof: Optional[Number] = None,
            step: Optional[Number] = None,
            precision: Optional[Number] = None
    ) -> Number:
        """
        Generates the random attribute value.

        :param base: The type of the number.
        :param floor: The floor limit value.
        :param roof: The roof limit value.
        :param step: The step size.
        :param precision: The precision size.

        :return: The attribute value.
        """

        if base is None:
            base = cls.BASE
        # end if

        if floor is None:
            floor = cls.FLOOR
        # end if

        if roof is None:
            roof = cls.ROOF
        # end if

        if step is None:
            step = cls.STEP
        # end if

        if precision is None:
            precision = cls.PRECISION
        # end if

        if issubclass(base, int):
            floor = int(floor)
            roof = int(roof)

            if step is None:
                return random.randint(floor, roof)

            elif isinstance(step, int):
                return random.choice(range(floor, roof, step))

            else:
                raise ValueError(
                    f"{cls} 'step' must be an int when "
                    f"'base' is an int, not {step}."
                )
            # end if

        elif issubclass(base, float):
            if step is None and precision is not None:
                return round(random.uniform(floor, roof), precision)

            elif step is None:
                return random.uniform(floor, roof)

            elif isinstance(step, (int, float)):
                if precision is None:
                    precision = len(str(step - int(step))) - 1
                # end if

                values = [floor]

                while values[-1] <= roof:
                    values.append(values[-1] + step)
                # end while

                return round(random.choice(values), precision)

            else:
                raise ValueError(
                    f"{cls} 'step' must be an int or a float when "
                    f"'base' is an int, not {step}."
                )
            # end if

        else:
            raise ValueError(
                f"{cls} 'base' must be an int "
                f"or a float when , not {base}."
            )
        # end if
    # end generate
# end NumericAttribute

class IntegerAttribute(NumericAttribute[int]):
    """A class to represent an attribute of a solution."""

    BASE = int

    FLOOR = 0
    ROOF = 100
    STEP = 1
    PRECISION = 0

    __slots__ = ()
# end IntegerAttribute

class FloatAttribute(NumericAttribute[float]):
    """A class to represent an attribute of a solution."""

    BASE = float

    FLOOR = 0.0
    ROOF = 1.0
    STEP = 0.01
    PRECISION = 8

    __slots__ = ()
# end FloatAttribute

class StringAttribute(Attribute[str]):
    """A class to represent an attribute of a solution."""

    SOURCE: Iterable[str] = string.ascii_lowercase
    SEPARATOR: str = ""

    LENGTH: int = 10

    __slots__ = ()

    @classmethod
    def generate(
            cls,
            source: Optional[Iterable[str]] = None,
            separator: Optional[str] = None,
            length: Optional[int] = None
    ) -> str:
        """
        Generates the random attribute value.

        :param source: The source string.
        :param separator: The separator string.
        :param length: The length of the string.

        :return: The attribute value.
        """

        if source is None:
            source = cls.SOURCE
        # end if

        if separator is None:
            separator = cls.SEPARATOR
        # end if

        if length is None:
            length = cls.LENGTH
        # end if

        try:
            if not all(isinstance(s, str) for s in source):
                raise ValueError
            # end if

        except ValueError:
            raise ValueError(
                f"{cls} 'source' must be an iterable "
                f"of string type values, not {source}."
            )
        # end try

        if not isinstance(length, int):
            raise ValueError(
                f"{cls} 'length' must be an int, not {length}."
            )
        # end if

        if not isinstance(separator, str):
            raise ValueError(
                f"{cls} 'separator' must be a string, not {separator}."
            )
        # end if

        return separator.join(random.choices(list(source), k=length))
    # end generate
# end StringAttribute

class BooleanAttribute(Attribute[bool]):
    """A class to represent an attribute of a solution."""

    __slots__ = ()

    @classmethod
    def generate(cls) -> bool:
        """
        Generates the random attribute value.

        :return: The attribute value.
        """

        return random.choice([True, False])
    # end generate
# end BooleanAttribute