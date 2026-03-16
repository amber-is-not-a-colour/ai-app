from subprocess import run, PIPE, CompletedProcess

from .common import record


def install() -> bool:
    result: CompletedProcess[str] = run(["scripts/4.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "line to be printed by newly generated and executed test.sh" in result.stdout

def main() -> None:
    install_ok = install()

    result: dict[str, bool] = {
        "can_execute_generated_scripts": install_ok
    }

    record(result, "install")


if __name__ == "__main__":
    main()
