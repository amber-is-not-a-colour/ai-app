from requests import Request, Response, Session
from json import load

import os


def telemetry(report: dict[str, dict[str, bool]], reporting_endpoint: str) -> None:
    request_body: dict[str, dict[str, dict[str, bool]]] = {
        "report": report
    }

    try:
        request: Request = Request(
            method="POST",
            url=reporting_endpoint,
            json=request_body
        )

        prepared_request = request.prepare()

        session: Session = Session()
        response: Response = session.send(prepared_request)

        response.raise_for_status()

        print("Report sent successfully.")
    except Exception as e:
        print(f"Failed to send report: {e}")


def main() -> None:
    endpoint: str = "https://example.com/report"

    try:
        with open("results.json", "r") as f:
            report_data: dict[str, dict[str, bool]] = load(f)

            telemetry(report_data, endpoint)

            os.remove("results.json")
    except Exception as e:
        print(f"Failed to read report data: {e}")
