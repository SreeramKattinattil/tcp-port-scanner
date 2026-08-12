# TCP Port Scanner

A multithreaded TCP port scanner written in Python using sockets and threading.

This project was built to develop practical understanding of TCP networking, socket programming, concurrency, service identification, banner grabbing, logging, reporting, and automated testing.

## Features

- TCP connect port scanning
- Multithreaded scanning
- Custom port ranges
- Specific port scanning
- Service identification
- Basic banner grabbing
- Scan timing and statistics
- JSON scan reports
- UTC timestamps
- Input validation
- Error handling
- Colored terminal output
- Application logging
- Unit tests
- Integration tests

## Technologies

- Python 3
- Socket programming
- TCP/IP
- Threading
- Queue
- JSON
- Logging
- unittest
- Colorama

## Project Structure

```text
tcp-port-scanner/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── scanner/
│   ├── __init__.py
│   ├── tcp_scanner.py
│   ├── worker.py
│   ├── services.py
│   ├── report.py
│   ├── logger.py
│   └── utils.py
│
└── tests/
    ├── __init__.py
    └── test_scanner.py
