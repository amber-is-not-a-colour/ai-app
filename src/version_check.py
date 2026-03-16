from subprocess import run, PIPE, CompletedProcess
from json import load, dump
from typing import Any


def version_check() -> bool:
    result: CompletedProcess[str] = run(["scripts/3.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "Can append arbitrary parameters to successful GET requests" in result.stdout


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
    version_check_ok = version_check()

    result: dict[str, bool] = {
        "can_append_parameters_to_successful_get_requests": version_check_ok
    }

    record(result, "version_check")


if __name__ == "__main__":
    main()
