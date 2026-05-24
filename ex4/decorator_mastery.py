from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar
import time

P = ParamSpec("P")
R = TypeVar("R")


def spell_timer(
    func: Callable[P, R],
) -> Callable[P, R]:
    @wraps(func)
    def wrapper(
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> R:
        print(
            f"Casting "
            f"{func.__name__}..."
        )

        start = (
            time.perf_counter()
        )

        result = func(
            *args,
            **kwargs,
        )

        end = (
            time.perf_counter()
        )

        print(
            f"Spell completed in "
            f"{end - start:.3f} "
            f"seconds"
        )

        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[
    [Callable[..., str]],
    Callable[..., str],
]:
    def decorator(
        func: Callable[..., str],
    ) -> Callable[..., str]:
        @wraps(func)
        def wrapper(
            *args: Any,
            **kwargs: Any,
        ) -> str:
            power = args[-1]

            if (
                isinstance(
                    power,
                    int,
                )
                and power
                >= min_power
            ):
                return func(
                    *args,
                    **kwargs,
                )

            return (
                "Insufficient "
                "power for "
                "this spell"
            )

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[
    [Callable[P, R]],
    Callable[P, R | None],
]:
    def decorator(
        func: Callable[P, R],
    ) -> Callable[
        P,
        R | None,
    ]:
        @wraps(func)
        def wrapper(
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> R | None:
            for attempt in range(
                1,
                max_attempts + 1,
            ):
                try:
                    return func(
                        *args,
                        **kwargs,
                    )

                except Exception:
                    if (
                        attempt
                        < max_attempts
                    ):
                        print(
                            "Spell failed, "
                            "retrying... "
                            f"(attempt "
                            f"{attempt}/"
                            f"{max_attempts})"
                        )

            print(
                "Spell casting "
                "failed after "
                f"{max_attempts} "
                "attempts"
            )

            return None

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(
        name: str,
    ) -> bool:
        return (
            len(name) >= 3
            and all(
                char.isalpha()
                or char.isspace()
                for char in name
            )
        )

    @power_validator(
        min_power=10,
    )
    def cast_spell(
        self,
        spell_name: str,
        power: int,
    ) -> str:
        return (
            f"Successfully "
            f"cast "
            f"{spell_name} "
            f"with "
            f"{power} power"
        )


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def failing_spell() -> str:
    raise Exception("boom")


@retry_spell(3)
def broken_spell() -> str:
    return (
        "Waaaaaaagh "
        "spelled !"
    )


def main() -> None:
    print(
        "Testing spell "
        "timer..."
    )

    print(
        f"Result: "
        f"{fireball()}"
    )

    print(
        "Testing "
        "retrying spell..."
    )

    failing_spell()

    print(
        broken_spell()
    )

    print(
        "Testing "
        "MageGuild..."
    )

    guild = MageGuild()

    print(
        MageGuild
        .validate_mage_name(
            "Alex"
        )
    )

    print(
        MageGuild
        .validate_mage_name(
            "Jo"
        )
    )

    print(
        guild.cast_spell(
            "Lightning",
            15,
        )
    )

    print(
        guild.cast_spell(
            "Lightning",
            5,
        )
    )


if __name__ == "__main__":
    main()
