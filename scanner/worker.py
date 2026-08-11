import socket

from scanner.services import get_service_name


def grab_banner(sock, port):
    """
    Attempt to retrieve a basic service banner.
    """

    try:

        if port in (80, 8080, 8000, 8008, 8888):

            request = (
                "HEAD / HTTP/1.0\r\n"
                "Host: localhost\r\n"
                "Connection: close\r\n"
                "\r\n"
            )

            sock.sendall(request.encode())

        banner = sock.recv(1024)

        if banner:

            return banner.decode(
                errors="replace"
            ).strip()

    except (
        socket.timeout,
        socket.error
    ):
        pass

    return None


def scan_port(target, port):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        sock.settimeout(0.5)

        result = sock.connect_ex(
            (target, port)
        )

        if result == 0:

            service = get_service_name(port)

            banner = grab_banner(
                sock,
                port
            )

            return {
                "port": port,
                "state": "open",
                "service": service,
                "banner": banner
            }

    except socket.error:

        pass

    finally:

        sock.close()

    return None
