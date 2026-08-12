import json
import os
from datetime import datetime, timezone


def save_json_report(target, ports_scanned, results, scan_time):
    """
    Save scan results to a JSON report using a UTC timestamp.
    """

    os.makedirs("reports", exist_ok=True)

    now = datetime.now(timezone.utc)

    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    safe_target = (
        target
        .replace("/", "_")
        .replace(":", "_")
    )

    filename = f"scan_{safe_target}_{timestamp}.json"

    filepath = os.path.join(
        "reports",
        filename
    )

    report = {
        "target": target,
        "scan_time_utc": now.isoformat(),
        "ports_scanned": ports_scanned,
        "open_ports": len(results),
        "duration_seconds": round(scan_time, 2),
        "results": results
    }

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    return filepath
