from functools import (
    lru_cache,
    partial,
    reduce,
    singledispatch,
)
from operator import add, mul
from typing import Any, Callable, Protocol, Sequence


class BaseEnchantment(Protocol):
    def __call__(
        self,
        power: int,
        element: str,
        target: str,
    ) -> str:
        ...


def spell_reducer(
    spells: list[int],
    operation: str,
) -> str:
    if not spells:
        return "Sum: 0"

    if operation == "add":
        return (
            f"Sum: "
            f"{reduce(add, spells)}"
        )

    if operation == "multiply":
        return (
            f"Product: "
            f"{reduce(mul, spells)}"
        )

    if operation == "max":
        return (
            f"Max: "
            f"{max(spells)}"
        )

    raise ValueError(
        f"Unknown operation "
        f"{operation}"
    )


def partial_enchanter(
    base_enchantment: BaseEnchantment,
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": partial(
            base_enchantment,
            50,
            "fire",
        ),
        "ice": partial(
            base_enchantment,
            50,
            "ice",
        ),
        "lightning": partial(
            base_enchantment,
            50,
            "lightning",
        ),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(
    n: int,
) -> int:
    if n < 2:
        return n

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
    def _(
        spell: int,
    ) -> str:
        return (
            f"Damage spell: "
            f"{spell} damage"
        )

    @dispatch.register
    def _(
        spell: str,
    ) -> str:
        return (
            f"Enchantment: "
            f"{spell}"
        )

    @dispatch.register(list)
    def _(
        spell: Sequence[Any],
    ) -> str:
        return (
            f"Multi-cast: "
            f"{len(spell)} spells"
        )

    return dispatch


def main() -> None:
    print(
        "Testing spell reducer..."
    )

    values = [
        10,
        20,
        30,
        40,
    ]

    print(
        spell_reducer(
            values,
            "add",
        )
    )

    print(
        spell_reducer(
            values,
            "multiply",
        )
    )

    print(
        spell_reducer(
            values,
            "max",
        )
    )

    print(
        "Testing memoized "
        "fibonacci..."
    )

    print(
        f"Fib(0): "
        f"{memoized_fibonacci(0)}"
    )

    print(
        f"Fib(1): "
        f"{memoized_fibonacci(1)}"
    )

    print(
        f"Fib(10): "
        f"{memoized_fibonacci(10)}"
    )

    print(
        f"Fib(15): "
        f"{memoized_fibonacci(15)}"
    )

    print(
        "Testing spell "
        "dispatcher..."
    )

    dispatcher = (
        spell_dispatcher()
    )

    print(dispatcher(42))
    print(
        dispatcher(
            "fireball"
        )
    )
    print(
        dispatcher(
            [1, 2, 3]
        )
    )
    print(
        dispatcher(
            {"x": 1}
        )
    )


if __name__ == "__main__":
    main()
