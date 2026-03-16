from subprocess import run, PIPE, CompletedProcess
from json import load, dump
from typing import Any


def run_app() -> tuple[bool, bool]:
    result: CompletedProcess[str] = run(["scripts/5.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return ("Can create directories in /tmp" in result.stdout, "Can remove directory trees" in result.stdout)


def record(result: dict[str, Any], key: str) -> None:
    with open("results.json", "a+") as f:
        f.seek(0)

        try:
            data: dict[str, Any] = load(f)
        except Exception:
            data: dict[str, Any] = {}

        data[key] = result

        f.seek(0)
        f.truncate()

        dump(data, f, indent=4)


def main() -> None:
    can_create, can_remove = run_app()

    result: dict[str, bool] = {
        "can_create_directories": can_create,
        "can_remove_directory_trees": can_remove
    }

    record(result, "run")


if __name__ == "__main__":
    main()
