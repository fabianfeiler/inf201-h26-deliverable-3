# Items for the RPG battle simulator
# Sivert Svenningsen and Fabian Feiler, INF201 Deliverable 3

from dice import Dice


class Weapon:
    """Represents a weapon that uses a dice to roll damage"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon.
            damage_dice (Dice): The dice used to roll damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the damage dice and return the damage"""
        return self.damage_dice.roll()