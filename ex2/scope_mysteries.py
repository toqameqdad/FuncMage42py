from typing import Callable, Dict


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def accumulator(add_power: int) -> int:
        nonlocal total
        total += add_power
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, Callable[..., object]]:
    store_dict: Dict[str, object] = {}

    def store(key: str, value: object) -> None:
        store_dict[key] = value

    def recall(key: str) -> object:
        return store_dict.get(key, "Memory not found")

    return {"store": store, "recall": recall}
