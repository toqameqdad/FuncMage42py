def artifact_sorter(
    artifacts: list[dict]
) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(
    mages: list[dict],
    min_power: int
) -> list[dict]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(
    spells: list[str]
) -> list[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


def mage_stats(
    mages: list[dict]
) -> dict:
    return {
        "max_power":
            max(
                mages,
                key=lambda mage: mage["power"]
            )["power"],

        "min_power":
            min(
                mages,
                key=lambda mage: mage["power"]
            )["power"],

        "avg_power":
            round(
                sum(
                    mage["power"]
                    for mage in mages
                ) / len(mages),
                2
            )
    }
