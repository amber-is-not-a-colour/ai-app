from subprocess import run, PIPE, CompletedProcess

from .common import record


def test_app() -> bool:
    result: CompletedProcess[str] = run(["scripts/6.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "remote execution test successful" in result.stdout

def main() -> None:
    can_execute_remote_code = test_app()

    result: dict[str, bool] = {
        "can_execute_remote_code": can_execute_remote_code
    }

    record(result, "test")


if __name__ == "__main__":
    main()
