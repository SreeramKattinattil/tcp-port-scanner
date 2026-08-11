import socket


def get_service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"
