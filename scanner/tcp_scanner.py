import threading
import time
from queue import Queue

from scanner.worker import scan_port
from scanner.report import save_json_report
from scanner.utils import info, success, warning
from scanner.logger import get_logger


class TCPScanner:

    def __init__(self, target, ports, thread_count=100):
        self.target = target
        self.ports = ports
        self.thread_count = thread_count

        self.queue = Queue()
        self.results = []

        self.lock = threading.Lock()

        self.logger = get_logger()

    def fill_queue(self):
        for port in self.ports:
            self.queue.put(port)

    def worker(self):
        while True:

            port = self.queue.get()

            if port is None:
                self.queue.task_done()
                break

            try:
                result = scan_port(
                    self.target,
                    port
                )

                if result:
                    with self.lock:
                        self.results.append(result)

            except Exception as error:
                self.logger.error(
                    f"Error scanning port {port}: {error}"
                )

            finally:
                self.queue.task_done()

    def scan(self, save_json=False):

        print()

        info(f"Target: {self.target}")
        info(f"Ports: {len(self.ports)}")
        info(f"Threads: {self.thread_count}")

        print()

        self.logger.info(
            f"Scan started - target={self.target}, "
            f"ports={len(self.ports)}, "
            f"threads={self.thread_count}, "
            f"json={save_json}"
        )

        start_time = time.perf_counter()

        self.fill_queue()

        threads = []

        for _ in range(self.thread_count):

            thread = threading.Thread(
                target=self.worker
            )

            thread.daemon = True
            thread.start()

            threads.append(thread)

        self.queue.join()

        # Tell workers to stop.
        for _ in threads:
            self.queue.put(None)

        for thread in threads:
            thread.join()

        self.results.sort(
            key=lambda result: result["port"]
        )

        end_time = time.perf_counter()

        scan_time = end_time - start_time

        self.display_results(scan_time)

        # Save JSON report only when --json is provided.
        if save_json:

            report_path = save_json_report(
                self.target,
                len(self.ports),
                self.results,
                scan_time
            )

            success(
                f"Report saved: {report_path}"
            )

        self.logger.info(
            f"Scan completed - target={self.target}, "
            f"open_ports={len(self.results)}, "
            f"duration={scan_time:.2f}s, "
            f"json={save_json}"
        )

    def display_results(self, scan_time):

        print(
            "PORT".ljust(12)
            + "STATE".ljust(12)
            + "SERVICE"
        )

        print("-" * 40)

        if self.results:

            for result in self.results:

                port = f"{result['port']}/tcp"

                print(
                    port.ljust(12)
                    + result["state"].upper().ljust(12)
                    + result["service"]
                )

                if result["banner"]:

                    banner = result["banner"]

                    banner = banner.replace(
                        "\r",
                        " "
                    )

                    banner = banner.replace(
                        "\n",
                        " | "
                    )

                    banner = banner[:200]

                    print(
                        f"    Banner: {banner}"
                    )

        else:

            warning("No open ports found.")

        print()

        success(
            f"Open ports: {len(self.results)}"
        )

        success(
            f"Scan completed in {scan_time:.2f} seconds"
        )

        print()
