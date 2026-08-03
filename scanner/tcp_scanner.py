class TCPScanner:

    def __init__(self, target):
        self.target = target

    def scan(self):
        print(f"Scanning {self.target}...")