"""
Module: battle
Description: Battle class for turn-based combat between two characters.
Author: Fabian Feiler and Sivert Svenningsen
Date: 2026-11-06
"""

from character import Character


class Battle:
    """Manages turn-based combat between a hero and an enemy."""

    def __init__(self, hero: Character, enemy: Character, max_rounds: int = 100) -> None:
        """
        Initialise the Battle.

        Args:
            hero (Character): The character who attacks first.
            enemy (Character): The opposing character.
            max_rounds (int): Limit to prevent endless battles (default = 100).
        """
        self.hero = hero
        self.enemy = enemy
        self.max_rounds = max_rounds
        self.round = 0

    def _attack(self, attacker: Character, defender: Character) -> None:
        """Let attacker attack defender and print the actual damage taken."""
        hp_before = defender.hp
        attacker.attack(defender)
        damage = hp_before - defender.hp
        print(f"{attacker.name} hits {defender.name} for {damage} damage ({defender.hp} HP left)")

    def play_round(self) -> None:
        """Hero attacks enemy, and if enemy survives, enemy attacks hero."""
        self.round += 1
        print(f"\nRound {self.round}")
        self._attack(self.hero, self.enemy)
        if self.enemy.is_alive:
            self._attack(self.enemy, self.hero)

    def simulate_battle(self) -> Character | None:
        """
        Run rounds until one character dies or max_rounds is reached.

        Returns:
            Character | None: The winner, or None if the battle ends in a draw.
        """
        while self.hero.is_alive and self.enemy.is_alive and self.round < self.max_rounds:
            self.play_round()

        if not self.enemy.is_alive:
            winner = self.hero
        elif not self.hero.is_alive:
            winner = self.enemy
        else:
            winner = None

        print(f"\nWinner: {winner.name}" if winner else "\nDraw: max rounds reached")
        return winner