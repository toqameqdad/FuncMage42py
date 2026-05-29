from collections.abc import Callable
from typing import List


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, str]]:
    def combined(
        target: str,
        power: int,
    ) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power),
        )

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int,
) -> Callable[[str, int], str]:
    def amplified(
        target: str,
        power: int,
    ) -> str:
        return base_spell(
            target,
            power * multiplier,
        )

    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def conditional(
        target: str,
        power: int,
    ) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: List[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    def sequence(
        target: str,
        power: int,
    ) -> list[str]:
        return [
            spell(target, power)
            for spell in spells
        ]

    return sequence


def fireball(
    target: str,
    power: int,
) -> str:
    return (
        f"Fireball hits "
        f"{target} for "
        f"{power} damage"
    )


def heal(
    target: str,
    power: int,
) -> str:
    return (
        f"Heal restores "
        f"{target} for "
        f"{power} HP"
    )


def strong_enough(
    target: str,
    power: int,
) -> bool:
    return power >= 50


def main() -> None:
    print("Testing spell combiner...")

    combined = spell_combiner(
        fireball,
        heal,
    )

    result1, result2 = combined(
        "Dragon",
        30,
    )

    print(
        "Combined spell result: "
        f"{result1}, "
        f"{result2}"
    )

    print("\nTesting power amplifier...")

    mega_fireball = power_amplifier(
        fireball,
        3,
    )

    print(
        "Amplified result: "
        f"{mega_fireball('Dragon', 10)}"
    )

    print("\nTesting conditional caster...")

    conditional = conditional_caster(
        strong_enough,
        fireball,
    )

    print(
        "Strong cast: "
        f"{conditional('Goblin', 70)}"
    )

    print(
        "Weak cast: "
        f"{conditional('Goblin', 20)}"
    )

    print("\nTesting spell sequence...")

    sequence = spell_sequence(
        [fireball, heal]
    )

    print(
        "Sequence result: "
        f"{sequence('Knight', 40)}"
    )


if __name__ == "__main__":
    main()
