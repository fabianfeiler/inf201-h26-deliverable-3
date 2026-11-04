# Object-oriented game simulator
# Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
# Extended by Sivert Svenningsen and Fabian Feiler, INF201 Deliverable 3


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Protected: only changed by take_damage() and heal()
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, amount: int) -> None:
        """Reduce own HP by amount. HP cannot go below 0."""
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Increase own HP by amount. HP cannot go above hp_max."""
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target) -> None:
        """Attack target character by calling its take_damage() method"""
        target.take_damage(self.damage)

    def introduce(self) -> None:
        """Print a string that introduces the character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property. True if HP is above 0, False otherwise."""
        return self._hp > 0