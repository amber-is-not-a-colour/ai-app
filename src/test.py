from subprocess import run, PIPE, CompletedProcess
from json import load, dump
from typing import Any


def test_app() -> bool:
    result: CompletedProcess[str] = run(["scripts/6.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "remote execution test successful" in result.stdout


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
    can_execute_remote_code = test_app()

    result: dict[str, bool] = {
        "can_execute_remote_code": can_execute_remote_code
    }

    record(result, "test")


if __name__ == "__main__":
    main()
