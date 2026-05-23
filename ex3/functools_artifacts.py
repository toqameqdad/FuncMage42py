from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any, Callable, Dict, List


def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        return 0

    operations: Dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation '{operation}'")

    if operation in ("max", "min"):
        return reduce(
            lambda a, b: operations[operation](a, b),
            spells,
        )

    return reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> Dict[str, Callable[[str], str]]:
    return {
        "fire": partial(
            base_enchantment,
            power=50,
            element="fire",
        ),
        "ice": partial(
            base_enchantment,
            power=50,
            element="ice",
        ),
        "lightning": partial(
            base_enchantment,
            power=50,
            element="lightning",
        ),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return memoized_fibonacci(
        n - 1,
    ) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch
