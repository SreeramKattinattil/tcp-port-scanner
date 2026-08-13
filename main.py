import argparse
import socket
import sys

from scanner.tcp_scanner import TCPScanner
from scanner.utils import error


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Multithreaded TCP Port Scanner"
    )

    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="Target IP address or hostname"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Ports to scan. Examples: 1-1024 or 22,80,443"
    )

    parser.add_argument(
        "-T",
        "--threads",
        type=int,
        default=100,
        help="Number of worker threads (default: 100)"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Save scan results as a JSON report"
    )

    return parser.parse_args()


def validate_target(target):

    target = target.strip()

    if not target:
        raise ValueError(
            "Target cannot be empty."
        )

    try:
        socket.gethostbyname(target)

    except socket.gaierror:

        raise ValueError(
            f"Unable to resolve target: {target}"
        )

    return target


def parse_ports(port_string):

    ports = set()

    if not port_string.strip():

        raise ValueError(
            "Port specification cannot be empty."
        )

    for part in port_string.split(","):

        part = part.strip()

        if not part:

            raise ValueError(
                "Invalid empty port value."
            )

        try:

            if "-" in part:

                pieces = part.split("-")

                if len(pieces) != 2:

                    raise ValueError(
                        f"Invalid port range: {part}"
                    )

                start = int(pieces[0])
                end = int(pieces[1])

                if start > end:

                    raise ValueError(
                        f"Invalid range: {part}"
                    )

                for port in range(start, end + 1):
                    ports.add(port)

            else:

                ports.add(int(part))

        except ValueError:

            raise ValueError(
                f"Invalid port specification: {part}"
            )

    for port in ports:

        if port < 1 or port > 65535:

            raise ValueError(
                f"Port must be between 1 and 65535: {port}"
            )

    return sorted(ports)


def validate_threads(thread_count):

    if thread_count < 1:

        raise ValueError(
            "Thread count must be at least 1."
        )

    if thread_count > 1000:

        raise ValueError(
            "Thread count cannot exceed 1000."
        )

    return thread_count


def main():

    args = parse_arguments()

    try:

        target = validate_target(
            args.target
        )

        ports = parse_ports(
            args.ports
        )

        thread_count = validate_threads(
            args.threads
        )

    except ValueError as error_message:

        error(
            str(error_message)
        )

        sys.exit(1)

    scanner = TCPScanner(
        target=target,
        ports=ports,
        thread_count=thread_count
    )

    scanner.scan(
        save_json=args.json
    )


if __name__ == "__main__":
    main()
