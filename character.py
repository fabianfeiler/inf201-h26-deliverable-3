"""
Object-oriented game simulator.

Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
Extended by Sivert Svenningsen and Fabian Feiler, INF201 Deliverable 3
"""

from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(
        self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None
    ) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
            weapon (Weapon | None): The weapon the character wields (default = None)
        """
        self.name = name
        self._hp = hp_max  # Protected: only changed by take_damage() and heal()
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """
        Reduce own HP by amount. HP cannot go below 0.

        Args:
            amount (int): The damage taken.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """
        Increase own HP by amount. HP cannot go above hp_max.

        Args:
            amount (int): The HP to heal.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Heal amount cannot be negative")
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target: "Character") -> None:
        """Attack target. Use the weapon if the character has one."""
        if self.weapon is not None:
            target.take_damage(self.weapon.roll_damage())
        else:
            target.take_damage(self.damage)

    def introduce(self) -> None:
        """Print a string that introduces the character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<{type(self).__name__} name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"{type(self).__name__}: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property. True if HP is above 0, False otherwise."""
        return self._hp > 0


class Warrior(Character):
    """Defensive character. Armor reduces incoming damage."""

    def __init__(
        self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, armor: int = 5
    ) -> None:
        """
        Initialise the Warrior

        Args:
            name (str): The name of the warrior.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when warrior attacks (default = 10)
            weapon (Weapon | None): The weapon the warrior wields (default = None)
            armor (int): Reduces incoming damage (default = 5)
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """
        Reduce damage by armor, then take the rest. Damage cannot be below 0.

        Args:
            amount (int): The damage before armor is applied.
        """
        reduced_damage = max(amount - self.armor, 0)
        super().take_damage(reduced_damage)


class Mage(Character):
    """Resource-based attacker. Uses mana for magic attacks."""

    def __init__(
        self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None,
        mana: int = 30, mana_max: int = 30
    ) -> None:
        """
        Initialise the Mage

        Args:
            name (str): The name of the mage.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when mage attacks (default = 10)
            weapon (Weapon | None): The weapon the mage wields (default = None)
            mana (int): Mana available for magic (default = 30)
            mana_max (int): Max mana (default = 30)
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: "Character") -> None:
        """Magic attack with double damage if mana >= 10. Otherwise base attack and restore 5 mana."""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(2 * self.damage)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)