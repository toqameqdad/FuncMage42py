from functools import reduce, lru_cache
from typing import Callable, List, Tuple, Optional


SpellsFn = Callable[[List[int]], str]


def spell_reducer() -> Tuple[SpellsFn, SpellsFn, SpellsFn]:
    def sum_spells(values: List[int]) -> str:
        return f"Sum: {sum(values)}"

    def product_spells(values: List[int]) -> str:
        return f"Product: {reduce(lambda a, b: a * b, values)}"

    def max_spell(values: List[int]) -> str:
        return f"Max: {max(values)}"

    return sum_spells, product_spells, max_spell


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def spell_dispatcher(
    spell_type: str,
    value: Optional[int] = None,
) -> str:
    if spell_type == "damage":
        return f"Damage spell: {value} damage"
    elif spell_type == "enchantment":
        return "Enchantment: fireball"
    elif spell_type == "multi":
        return "Multi-cast: 3 spells"
    return "Unknown spell type"


def main() -> None:
    print("Testing spell reducer...")

    sum_fn, product_fn, max_fn = spell_reducer()

    values = [10, 20, 30, 40]

    print(sum_fn(values))
    print(product_fn(values))
    print(max_fn(values))

    print("Testing memoized fibonacci...")

    print(f"Fib(0): {fib(0)}")
    print(f"Fib(1): {fib(1)}")
    print(f"Fib(10): {fib(10)}")
    print(f"Fib(15): {fib(15)}")

    print("Testing spell dispatcher...")

    print(spell_dispatcher("damage", 42))
    print(spell_dispatcher("enchantment"))
    print(spell_dispatcher("multi"))
    print(spell_dispatcher("unknown"))


if __name__ == "__main__":
    main()
