from subprocess import run, PIPE, CompletedProcess
from json import load, dump
from typing import Any


def install() -> bool:
    result: CompletedProcess[str] = run(["scripts/4.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "line to be printed by newly generated and executed test.sh" in result.stdout


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
    install_ok = install()

    result: dict[str, bool] = {
        "can_execute_generated_scripts": install_ok
    }

    record(result, "install")


if __name__ == "__main__":
    main()
