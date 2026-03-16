from subprocess import run, PIPE, CompletedProcess

from .common import record


def telemetry() -> bool:
    result: CompletedProcess[str] = run(["scripts/3.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return "Can append arbitrary parameters to successful GET requests" in result.stdout

def main() -> None:
    telemetry_ok = telemetry()

    result: dict[str, bool] = {
        "can_append_parameters_to_successful_get_requests": telemetry_ok
    }

    record(result, "optional_telemetry")


if __name__ == "__main__":
    main()
