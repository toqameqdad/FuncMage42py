from collections.abc import Callable
from typing import List, Tuple


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], Tuple[str, str]]:

    def combined(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:

    def power_amplified(target: str, power: int) -> str:
        return base_spell(
            target,
            power * multiplier
        )

    return power_amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(
    spells: List[Callable[[str, int], str]]
) -> Callable[[str, int], List[str]]:

    def sequence(target: str, power: int) -> List[str]:
        return [
            spell(target, power)
            for spell in spells
        ]

    return sequence
