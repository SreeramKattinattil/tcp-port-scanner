import unittest
import socket

from main import parse_ports, validate_target, validate_threads
from scanner.services import get_service_name


class TestPortParser(unittest.TestCase):

    def test_single_port(self):
        result = parse_ports("80")

        self.assertEqual(result, [80])

    def test_multiple_ports(self):
        result = parse_ports("22,80,443")

        self.assertEqual(
            result,
            [22, 80, 443]
        )

    def test_port_range(self):
        result = parse_ports("1-5")

        self.assertEqual(
            result,
            [1, 2, 3, 4, 5]
        )

    def test_mixed_ports(self):
        result = parse_ports("22,80,100-102")

        self.assertEqual(
            result,
            [22, 80, 100, 101, 102]
        )

    def test_duplicate_ports(self):
        result = parse_ports("80,80,80")

        self.assertEqual(
            result,
            [80]
        )

    def test_invalid_port(self):
        with self.assertRaises(ValueError):
            parse_ports("70000")

    def test_invalid_port_text(self):
        with self.assertRaises(ValueError):
            parse_ports("abc")

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            parse_ports("100-1")


class TestTargetValidation(unittest.TestCase):

    def test_valid_ip(self):
        result = validate_target("127.0.0.1")

        self.assertEqual(
            result,
            "127.0.0.1"
        )

    def test_localhost(self):
        result = validate_target("localhost")

        self.assertEqual(
            result,
            "localhost"
        )

    def test_invalid_target(self):
        with self.assertRaises(ValueError):
            validate_target(
                "this-target-does-not-exist.invalid"
            )


class TestThreadValidation(unittest.TestCase):

    def test_valid_threads(self):
        self.assertEqual(
            validate_threads(100),
            100
        )

    def test_zero_threads(self):
        with self.assertRaises(ValueError):
            validate_threads(0)

    def test_negative_threads(self):
        with self.assertRaises(ValueError):
            validate_threads(-1)

    def test_too_many_threads(self):
        with self.assertRaises(ValueError):
            validate_threads(1001)


class TestServiceDetection(unittest.TestCase):

    def test_http_service(self):
        service = get_service_name(80)

        self.assertEqual(
            service,
            "http"
        )

    def test_https_service(self):
        service = get_service_name(443)

        self.assertEqual(
            service,
            "https"
        )

    def test_ssh_service(self):
        service = get_service_name(22)

        self.assertEqual(
            service,
            "ssh"
        )


class TestPortConnection(unittest.TestCase):

    def test_localhost_connection(self):

        server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        server.bind(
            ("127.0.0.1", 0)
        )

        server.listen(1)

        port = server.getsockname()[1]

        client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        client.settimeout(1)

        result = client.connect_ex(
            ("127.0.0.1", port)
        )

        client.close()
        server.close()

        self.assertEqual(
            result,
            0
        )


if __name__ == "__main__":
    unittest.main()
