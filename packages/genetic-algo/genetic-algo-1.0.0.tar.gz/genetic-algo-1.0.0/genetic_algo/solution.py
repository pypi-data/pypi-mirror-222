# solution.py

from typing import (
    Self, Iterable, Optional, Type,
    List, Union, Generic, TypeVar
)

from represent import represent

from genetic_algo.attributes import Attribute

__all__ = [
    "Solution",
    "Template",
    "eliminate_repetitions",
    "same_solution"
]

@represent
class Solution:
    """A class to represent a solution of a problem."""

    __slots__ = "attributes", "fitness"

    def __init__(self, attributes: Iterable[Attribute]) -> None:
        """
        Defines the class attributes.

        :param attributes: The attributes of the solution.
        """

        self.attributes = list(attributes)

        self.fitness: Optional[float] = None
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

        return (type(self) is type(other)) and all(
            attr1 == attr2 for attr1, attr2 in
            zip(self.attributes, other.attributes)
        )
    # end __eq__

    @classmethod
    def build(cls, attributes: Iterable[Attribute]) -> Self:
        """
        Builds the solution from the class.

        :param attributes: The attributes of the solution.

        :return: The solution object.
        """

        return Solution(attributes=attributes)
    # end build
# end Solution

def same_solution(*solutions: Solution) -> bool:
    """
    Checks if all the given solutions are the same.

    :param solutions: The solutions to check.

    :return: The value of equality.
    """

    for sol1, sol2 in zip(solutions[:-1], solutions[1:]):
        if sol1 == sol2:
            return False
        # end if
    # end for

    return True
# end same_solution

def eliminate_repetitions(solutions: Iterable[Solution]) -> List[Solution]:
    """
    Removes the repeated solutions.

    :param solutions: The solutions to filter.

    :return: The unique solutions.
    """

    unique: List[Solution] = []

    for slo1 in solutions:
        for sol2 in unique:
            if slo1 == sol2:
                break
            # end if

        else:
            unique.append(slo1)
        # end if
    # end for

    return unique
# end eliminate_repetitions

_S = TypeVar("_S")

Attributes = List[
    Union[
        Union[Attribute, Type[Attribute]],
        Iterable[Union[Attribute, Type[Attribute]]]
    ]
]

@represent
class Template(Generic[_S]):
    """A class to represent a template for solution attributes."""

    SOLUTION: _S = Solution
    ATTRIBUTES: Attributes = []

    __slots__ = "solution", "attributes"

    def __init__(
            self,
            solution: Optional[Type[_S]] = None,
            attributes: Optional[Attributes] = None
    ) -> None:
        """
        Defines the class attributes.

        :param solution: The type of the solution object.
        :param attributes: The attributes of the solution.
        """

        self.solution: Type[_S] = solution or self.SOLUTION

        self.attributes: Attributes = list(attributes or []) or self.ATTRIBUTES
    # end __init__

    def build(self) -> _S:
        """
        Generates the random attribute.

        :return: The attribute object.
        """

        attributes = []

        for attribute in self.attributes:
            if issubclass(attribute, Attribute):
                attribute = attribute.build(
                    *attribute.arguments.args,
                    **attribute.arguments.kwargs
                )

            elif isinstance(attributes, Attribute):
                attribute = attribute.copy()

            else:
                try:
                    values = list(attribute)

                    attribute = (
                        type(values[0])
                        if isinstance(values[0], Attribute) else
                        values[0]
                    )(
                        value=Template(
                            solution=self.solution,
                            attributes=values
                        ).build().attributes
                    )

                except (ValueError, TypeError) as e:
                    raise ValueError(
                        f"Invalid attributes structure: "
                        f"{attribute}. {str(e)}"
                    )
                # end try
            # end if

            attributes.append(attribute)
        # end for

        return self.solution.build(attributes=attributes)
    # end build
# end Template