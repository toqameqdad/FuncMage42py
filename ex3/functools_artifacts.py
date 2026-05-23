from functools import (
    lru_cache,
    partial,
    reduce,
    singledispatch,
)
from operator import add, mul
from typing import (
    Any,
    Callable,
    Dict,
    List,
)


def spell_reducer(
    spells: List[int],
    operation: str,
) -> int:
    if not spells:
        return 0

    ops: Dict[
        str,
        Callable[[int, int], int],
    ] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in ops:
        raise ValueError(
            f"Unknown operation "
            f"{operation}"
        )

    if operation in (
        "max",
        "min",
    ):
        return reduce(
            lambda a, b:
            ops[operation](a, b),
            spells,
        )

    return reduce(
        ops[operation],
        spells,
    )


def partial_enchanter(
    base_enchantment:
    Callable[
        [int, str, str],
        str,
    ],
) -> Dict[
    str,
    Callable[[str], str],
]:
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
def memoized_fibonacci(
    n: int,
) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


def spell_dispatcher(
) -> Callable[[Any], str]:
    @singledispatch
    def dispatch(
        spell: Any,
    ) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return (
            f"Damage spell: "
            f"{spell} damage"
        )

    @dispatch.register
    def _(spell: str) -> str:
        return (
            f"Enchantment: "
            f"{spell}"
        )

    @dispatch.register
    def _(
        spell: list[Any],
    ) -> str:
        return (
            f"Multi-cast: "
            f"{len(spell)} spells"
        )

    return dispatch
