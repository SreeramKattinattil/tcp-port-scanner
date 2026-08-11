import threading
import time
from queue import Queue

from scanner.worker import scan_port
from scanner.report import save_json_report
from scanner.utils import info, success, warning


class TCPScanner:

    def __init__(self, target, ports, thread_count=100):
        self.target = target
        self.ports = ports
        self.thread_count = thread_count

        self.queue = Queue()
        self.results = []

        self.lock = threading.Lock()

    def fill_queue(self):
        for port in self.ports:
            self.queue.put(port)

    def worker(self):
        while True:

            port = self.queue.get()

            if port is None:
                self.queue.task_done()
                break

            result = scan_port(
                self.target,
                port
            )

            if result:

                with self.lock:
                    self.results.append(result)

            self.queue.task_done()

    def scan(self):

        print()

        info(f"Target: {self.target}")
        info(f"Ports: {len(self.ports)}")
        info(f"Threads: {self.thread_count}")

        print()

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

        report_path = save_json_report(
            self.target,
            len(self.ports),
            self.results,
            scan_time
        )

        success(
            f"Report saved: {report_path}"
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
