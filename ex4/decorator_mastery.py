from functools import wraps
from typing import Any, Callable
import time


def spell_timer(
    func: Callable[..., Any],
) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(
            f"Spell completed in "
            f"{end - start:.3f} seconds"
        )

        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any],
]:
    def decorator(
        func: Callable[..., Any],
    ) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(
            power: int,
            *args: Any,
            **kwargs: Any,
        ) -> Any:
            if power >= min_power:
                return func(
                    power,
                    *args,
                    **kwargs,
                )

            return (
                "Insufficient power "
                "for this spell"
            )

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[
    [Callable[..., Any]],
    Callable[..., Any],
]:
    def decorator(
        func: Callable[..., Any],
    ) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(
            *args: Any,
            **kwargs: Any,
        ) -> Any:
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
                    if attempt < max_attempts:
                        print(
                            "Spell failed, "
                            "retrying... "
                            f"(attempt "
                            f"{attempt}/"
                            f"{max_attempts})"
                        )
                    else:
                        return (
                            "Spell casting "
                            f"failed after "
                            f"{max_attempts} "
                            "attempts"
                        )

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
                c.isalpha()
                or c.isspace()
                for c in name
            )
        )

    @power_validator(min_power=10)
    def cast_spell(
        self,
        spell_name: str,
        power: int,
    ) -> str:
        return (
            f"Successfully cast "
            f"{spell_name} "
            f"with {power} power"
        )
