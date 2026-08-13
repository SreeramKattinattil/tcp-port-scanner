# TCP Port Scanner

A multithreaded TCP port scanner built with Python for network scanning, service identification, banner grabbing, logging, and JSON reporting.

> **Project status:** ✅ Completed — v1.0.0

---

## 🎯 Overview

The TCP Port Scanner is a Python-based network security tool that scans TCP ports on a target IP address or hostname and identifies open services.

The project was built to develop practical understanding of:

* TCP socket programming
* Network port scanning
* Multithreading
* Service detection
* Banner grabbing
* Input validation
* Logging
* Structured JSON reporting
* Automated testing

This project is intended for **educational purposes, authorized security testing, and network administration**.

---

## ✨ Features

* 🔎 TCP port scanning
* ⚡ Multithreaded scanning for improved performance
* 🎯 Scan individual ports or custom port ranges
* 🔧 Configurable number of worker threads
* 🛠️ Service identification
* 📡 Banner grabbing
* 📄 JSON scan reports
* 📝 Application logging
* ✅ Target and port input validation
* 🧪 Unit and integration tests
* 📊 Scan statistics and completion time

---

## 🛠️ Technologies

* **Python 3**
* **Socket Programming**
* **Threading**
* **argparse**
* **JSON**
* **unittest**
* **Logging**

---

## 📁 Project Structure

```text
tcp-port-scanner/
│
├── docs/
│   └── screenshots/
│       ├── basic-scan.png
│       ├── json-report.png
│       └── tests.png
│
├── scanner/
│   ├── __init__.py
│   ├── logger.py
│   ├── report.py
│   ├── services.py
│   ├── tcp_scanner.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_scanner.py
│
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── requirements.txt
```

---

## ⚙️ Requirements

* Python 3.8+
* Linux, macOS, or Windows
* Network access to the authorized target

Check your Python version:

```bash
python3 --version
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/SreeramKattinattil/tcp-port-scanner.git
```

Move into the project directory:

```bash
cd tcp-port-scanner
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

Display the available options:

```bash
python3 main.py --help
```

### Scan a port range

```bash
python3 main.py -t 127.0.0.1 -p 1-1000
```

### Scan specific ports

```bash
python3 main.py -t 127.0.0.1 -p 22,80,443
```

### Configure the number of threads

```bash
python3 main.py -t 127.0.0.1 -p 1-1000 -T 200
```

### Generate a JSON report

Use the JSON reporting option implemented in the current version:

```bash
python3 main.py -t 127.0.0.1 -p 1-1000 --json
```

> If your final CLI uses a different option name for JSON output, replace `--json` above with the exact option shown by `python3 main.py --help`.

---

## 📸 Screenshots

### Basic Port Scan

![Basic Port Scan](docs/screenshots/basic-scan.png)

### JSON Report

![JSON Report](docs/screenshots/json-report.png)

### Test Results

![Test Results](docs/screenshots/tests.png)

---

## 🧪 Testing

The project includes unit and integration tests covering:

* Port parsing
* Invalid ports
* Port ranges
* Duplicate ports
* Service detection
* TCP scanner functionality
* Target validation
* Thread validation

Run the complete test suite:

```bash
python3 -m unittest discover -v
```

### Test Result

The current test suite contains **19 tests**, all passing successfully.

```text
----------------------------------------------------------------------
Ran 19 tests in 0.027s

OK
```

---

## 🔐 Security Considerations

The scanner uses TCP socket connections to determine whether ports are accessible and to identify services.

The project is designed for controlled and authorized environments.

Do not use this tool to scan systems or networks without permission.

---

## ⚠️ Authorized Use

This tool is intended for:

* Educational cybersecurity labs
* Systems you own
* Authorized penetration testing
* Network administration
* Security research in controlled environments

**Only scan systems for which you have explicit authorization.**

The author is not responsible for unauthorized or illegal use of this software.

---

## 📚 Learning Outcomes

Building this project helped develop practical understanding of:

* TCP/IP networking
* TCP socket connections
* Port scanning techniques
* Python concurrency
* Multithreaded programming
* Network service identification
* Banner grabbing
* CLI application development
* Input validation
* Error handling
* Logging
* JSON data processing
* Unit and integration testing
* Git and GitHub project management

---

## 🔮 Future Improvements

Potential future improvements include:

* UDP scanning
* Improved service fingerprinting
* Configurable connection timeouts
* Additional report formats
* Scan result filtering
* More comprehensive test coverage
* Performance benchmarking

---

## 👨‍💻 Author

**Sreeram Kattinattil**

Aspiring VAPT | Offensive Security | SOC Analyst

GitHub: [SreeramKattinattil](https://github.com/SreeramKattinattil)

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
