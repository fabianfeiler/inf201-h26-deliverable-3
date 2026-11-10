"""
Module: dice
Description: Dice class for random damage rolls in the RPG.
Author: Fabian Feiler and Sivert Svenningsen
Date: 2026-11-04
"""

import random


class Dice:
    """An n-sided dice (n >= 2)."""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice.

        Args:
            sides (int): Number of sides (default = 6).

        Raises:
            ValueError: If sides is less than 2.
        """
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")
        self.sides = sides

    def roll(self) -> int:
        """
        Roll the dice.

        Returns:
            int: A random number from 1 to sides.
        """
        return random.randint(1, self.sides)

    def __call__(self) -> int:
        """Roll the dice by calling the object directly, e.g. d20()."""
        return self.roll()

    def __repr__(self) -> str:
        """Representation of the dice object, e.g. Dice(sides=6)."""
        return f"Dice(sides={self.sides})"