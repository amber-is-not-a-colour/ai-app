from subprocess import run, PIPE, CompletedProcess
from json import load, dump
from typing import Any


def check_dependencies() -> bool:
    result: CompletedProcess[str] = run(["scripts/2.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "Can connect to arbitrary web servers" in result.stdout


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
    dependencies_ok = check_dependencies()

    result: dict[str, bool] = {
        "can_connect_to_web": dependencies_ok
    }

    record(result, "dep_checks")


if __name__ == "__main__":
    main()
