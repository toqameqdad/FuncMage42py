from collections.abc import Callable


def spell_combiner(
    spell1: Callable,
    spell2: Callable
) -> Callable:

    def combined(
        target: str,
        power: int
    ):
        return (
            spell1(target, power),
            spell2(target, power)
        )

    return combined


def power_amplifier(
    base_spell: Callable,
    multiplier: int
) -> Callable:

    def power_amplified(
        target: str,
        power: int
    ) -> str:
        return base_spell(
            target,
            power * multiplier
        )

    return power_amplified


def conditional_caster(
    condition: Callable,
    spell: Callable
) -> Callable:

    def conditional_spell(
        target: str,
        power: int
    ):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(
    spells: list[Callable]
) -> Callable:

    def sequence(
        target: str,
        power: int
    ):
        results = []

        for spell in spells:
            results.append(
                spell(target, power)
            )

        return results

    return sequence
