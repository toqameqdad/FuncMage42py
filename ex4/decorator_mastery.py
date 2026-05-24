from functools import wraps
from typing import Callable, TypeVar, ParamSpec
import time

P = ParamSpec("P")
R = TypeVar("R")


def spell_timer(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Casting {func.__name__}...")

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[P, R]], Callable[P, R | None]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R | None]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | None:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            print(f"Spell casting failed after {max_attempts} attempts")
            return None

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace()
            for char in name
        )

    def cast_spell(self, spell_name: str, power: int) -> str:
        if power >= 10:
            return f"Successfully cast {spell_name} with {power} power"
        return "Insufficient power for this spell"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Result: Fireball cast!"


@retry_spell(3)
def failing_spell() -> str:
    raise Exception("boom")


@retry_spell(3)
def broken_spell() -> str:
    return "Waaaaaaagh spelled !"


def main() -> None:
    print("Testing spell timer...")
    print(fireball())

    print("Testing retrying spell...")
    failing_spell()
    print(broken_spell())

    print("Testing MageGuild...")

    guild = MageGuild()

    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("Jo"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
