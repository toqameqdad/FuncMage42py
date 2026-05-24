from collections.abc import Callable
from typing import List


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def combined(target: str, power: int) -> str:
        return (
            "Combined spell result: "
            f"{spell1(target, power)}, "
            f"{spell2(target, power)}"
        )

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int,
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return f"Original: {power}, Amplified: {power * multiplier}"

    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: List[Callable[[str, int], str]],
) -> Callable[[str, int], str]:
    def sequence(target: str, power: int) -> str:
        return " | ".join(
            spell(target, power)
            for spell in spells
        )

    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def strong_enough(target: str, power: int) -> bool:
    return power >= 50


def main() -> None:
    print("Testing spell combiner...")

    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 30))

    print("\nTesting power amplifier...")

    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")

    conditional = conditional_caster(strong_enough, fireball)

    print(conditional("Goblin", 70))
    print(conditional("Goblin", 20))

    print("\nTesting spell sequence...")

    sequence = spell_sequence([fireball, heal])
    print(sequence("Knight", 40))


if __name__ == "__main__":
    main()
