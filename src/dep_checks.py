from subprocess import run, PIPE, CompletedProcess

from .common import record


def check_dependencies() -> bool:
    result: CompletedProcess[str] = run(["scripts/2.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "Can connect to arbitrary web servers" in result.stdout

def main() -> None:
    dependencies_ok = check_dependencies()

    result: dict[str, bool] = {
        "can_connect_to_web": dependencies_ok
    }

    record(result, "dep_checks")


if __name__ == "__main__":
    main()
