from typing import TypedDict, List


class Artifact(TypedDict):
    name: str
    power: int
    type: str


class Mage(TypedDict):
    name: str
    power: int
    element: str


def artifact_sorter(artifacts: List[Artifact]) -> List[Artifact]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: List[Mage], min_power: int) -> List[Mage]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(spells: List[str]) -> List[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


def mage_stats(mages: List[Mage]) -> dict[str, float]:
    if not mages:
        return {"max_power": 0.0, "min_power": 0.0, "avg_power": 0.0}
    powers = [mage["power"] for mage in mages]
    return {
        "max_power": float(max(powers)),
        "min_power": float(min(powers)),
        "avg_power": round(sum(powers) / len(powers), 2)
    }
