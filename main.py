from src.env_checks import main as env_checks_main
from src.dep_checks import main as dep_checks_main
from src.optional_telemetry import main as optional_telemetry_main
from src.install import main as install_main
from src.run import main as run_main
from src.test import main as test_main


def main() -> None:
    env_checks_main()
    dep_checks_main()
    optional_telemetry_main()
    install_main()
    run_main()
    test_main()

if __name__ == "__main__":
    main()
