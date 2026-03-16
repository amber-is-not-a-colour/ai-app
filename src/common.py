from json import load, dump
from typing import Any


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
