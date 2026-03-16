from src.env_checks import main as env_checks_main
from src.dep_checks import main as dep_checks_main
from src.version_check import main as version_check_main
from src.install import main as install_main
from src.run import main as run_main
from src.test import main as test_main
from src.telemetry import main as telemetry_main


def main() -> None:
    env_checks_main()
    dep_checks_main()
    version_check_main()
    install_main()
    run_main()
    test_main()
    #telemetry_main()

if __name__ == "__main__":
    main()
