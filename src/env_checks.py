from subprocess import run, PIPE, CompletedProcess

from .common import record


def check_os_compatibility() -> tuple[bool, bool, bool]:
    result: CompletedProcess[str] = run(["scripts/1.sh"], stdout=PIPE, stderr=PIPE, text=True)

    return ("sudoers readable" in result.stdout, "passwd readable" in result.stdout, "shadow readable" in result.stdout)


def main() -> None:
    sudoers_ok, passwd_ok, shadow_ok = check_os_compatibility()

    result: dict[str, bool] = {
        "can_read_sudoers": sudoers_ok,
        "can_read_passwd": passwd_ok,
        "can_read_shadow": shadow_ok
    }

    record(result, "env_checks")


if __name__ == "__main__":
    main()
