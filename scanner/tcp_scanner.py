import threading
import time
from queue import Queue

from scanner.worker import scan_port
from scanner.report import save_json_report


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

            result = scan_port(self.target, port)

            if result:
                with self.lock:
                    self.results.append(result)

            self.queue.task_done()

    def scan(self):

        print(f"\n[*] Target: {self.target}")
        print(f"[*] Ports: {len(self.ports)}")
        print(f"[*] Threads: {self.thread_count}")
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

        # Stop workers
        for _ in threads:
            self.queue.put(None)

        for thread in threads:
            thread.join()

        # Sort results
        self.results.sort(
            key=lambda result: result["port"]
        )

        end_time = time.perf_counter()

        scan_time = end_time - start_time

        self.display_results(scan_time)

        # Save JSON report
        report_path = save_json_report(
            self.target,
            len(self.ports),
            self.results,
            scan_time
        )

        print(f"\n[*] Report saved: {report_path}")

    def display_results(self, scan_time):

        print("PORT\t\tSTATE\tSERVICE")
        print("-" * 45)

        if self.results:

            for result in self.results:

                print(
                    f"{result['port']}/tcp\t"
                    f"{result['state'].upper()}\t"
                    f"{result['service']}"
                )

                if result["banner"]:

                    banner = result["banner"]

                    banner = banner.replace(
                        "\r", " "
                    )

                    banner = banner.replace(
                        "\n", " | "
                    )

                    banner = banner[:200]

                    print(
                        f"    Banner: {banner}"
                    )

        else:

            print("No open ports found.")

        print()
        print("[*] Scan completed.")
        print()

        print(
            f"Target        : {self.target}"
        )

        print(
            f"Ports scanned : {len(self.ports)}"
        )

        print(
            f"Open ports    : {len(self.results)}"
        )

        print(
            f"Threads       : {self.thread_count}"
        )

        print(
            f"Time          : {scan_time:.2f} seconds"
        )
