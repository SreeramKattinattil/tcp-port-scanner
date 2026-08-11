from colorama import Fore, Style, init


# Automatically handles Windows terminal colors.
init(autoreset=True)


def info(message):
    print(f"{Fore.CYAN}[*] {message}{Style.RESET_ALL}")


def success(message):
    print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")


def warning(message):
    print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")


def error(message):
    print(f"{Fore.RED}[!] {message}{Style.RESET_ALL}")


def open_port(port, service):
    print(
        f"{Fore.GREEN}"
        f"[+] {port}/tcp OPEN {service}"
        f"{Style.RESET_ALL}"
    )
