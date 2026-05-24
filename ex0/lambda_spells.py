from typing import List, TypedDict


class Artifact(TypedDict):
    name: str
    power: int
    type: str


class Mage(TypedDict):
    name: str
    power: int
    element: str


def artifact_sorter(
    artifacts: List[Artifact],
) -> List[Artifact]:
    return sorted(
        artifacts,
        key=lambda a: a["power"],
        reverse=True,
    )


def power_filter(
    mages: List[Mage],
    min_power: int,
) -> List[Mage]:
    return list(
        filter(
            lambda m: m["power"] >= min_power,
            mages,
        )
    )


def spell_transformer(
    spells: List[str],
) -> List[str]:
    return list(
        map(
            lambda s: f"* {s} *",
            spells,
        )
    )


def mage_stats(
    mages: List[Mage],
) -> dict[str, float]:
    if not mages:
        return {
            "max_power": 0.0,
            "min_power": 0.0,
            "avg_power": 0.0,
        }

    powers = [m["power"] for m in mages]

    return {
        "max_power": float(max(powers)),
        "min_power": float(min(powers)),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts: List[Artifact] = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ice Wand", "power": 70, "type": "focus"},
    ]

    spells = [
        "fireball",
        "heal",
        "shield",
    ]

    print("Testing artifact sorter...")

    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("Testing spell transformer...")

    transformed = spell_transformer(spells)

    print(" ".join(transformed))


if __name__ == "__main__":
    main()
