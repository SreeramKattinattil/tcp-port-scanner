import json
import os
from datetime import datetime


def save_json_report(target, ports_scanned, results, scan_time):
    """
    Save scan results to a JSON file.
    """

    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Create a timestamp for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Replace characters that are not suitable for filenames
    safe_target = target.replace("/", "_").replace(":", "_")

    filename = f"scan_{safe_target}_{timestamp}.json"

    filepath = os.path.join("reports", filename)

    report = {
        "target": target,
        "scan_time": datetime.now().isoformat(),
        "ports_scanned": ports_scanned,
        "open_ports": len(results),
        "duration_seconds": round(scan_time, 2),
        "results": results
    }

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return filepath
