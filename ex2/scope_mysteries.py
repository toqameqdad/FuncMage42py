from typing import Dict
from collections.abc import Callable


def mage_counter() -> Callable[[], str]:
    count = 0

    def counter() -> str:
        nonlocal count
        count += 1
        return f"counter_a call {count}: {count}"

    return counter


def spell_accumulator(
    initial_power: int,
) -> Callable[[int], str]:
    total = initial_power

    def accumulator(add_power: int) -> str:
        nonlocal total
        total += add_power
        return f"Base {initial_power}, add {add_power}: {total}"

    return accumulator


def enchantment_factory(
    enchantment_type: str,
) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, Callable[..., object]]:
    store_dict: Dict[str, object] = {}

    def store(key: str, value: object) -> None:
        store_dict[key] = value
        print(f"Store ’{key}’ = {value}")

    def recall(key: str) -> str:
        if key in store_dict:
            return f"Recall ’{key}’: {store_dict[key]}"
        return "Recall ’unknown’: Memory not found"

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    print("Testing mage counter...")

    counter_a = mage_counter()
    counter_b = mage_counter()

    print(counter_a())
    print(counter_a())
    print(counter_b())

    print("\nTesting spell accumulator...")

    accumulator = spell_accumulator(100)

    print(accumulator(20))
    print(accumulator(30))

    print("\nTesting enchantment factory...")

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")

    vault = memory_vault()

    vault["store"]("secret", 42)

    print(vault["recall"]("secret"))
    print(vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
