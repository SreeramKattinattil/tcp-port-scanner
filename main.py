from scanner.tcp_scanner import TCPScanner

def main():
    target = input("Enter target IP or hostname: ").strip()

    scanner = TCPScanner(target)
    scanner.scan()

if __name__ == "__main__":
    main()