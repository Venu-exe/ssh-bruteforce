# SSH Brute Force Tool

> or educational purposes only. Use only on systems you own or have explicit permission to test. Unauthorized use is illegal.

## Description
A multi-threaded SSH brute force tool built in Python.
Designed for penetration testing and security research on authorized systems.

## Installation

### Clone the repo
```bash
git clone https://github.com/Venu-exe/ssh-bruteforce.git
cd ssh-bruteforce
```

### Install dependencies
```bash
pip install paramiko termcolor pyfiglet
```

## Usage
```bash
python3 brutefource.py
```



## Features
- Multi-threaded for fast brute forcing
- ASCII banner with author info
- Color coded output
- Timeout handling
- Graceful Ctrl+C exit
- Auto directory detection
- Skips blank passwords

## Dependencies
| Library | Purpose |
|---------|---------|
| paramiko | SSH connection handling |
| termcolor | Colored terminal output |
| pyfiglet | ASCII art banner |
| threading | Multi-thread support |
| socket | Network connection |

## Legal Disclaimer
This tool is intended for **legal and educational purposes only**.
- Only use on systems you **own**
- Only use with **explicit permission**
- The author is **not responsible** for any misuse

## Author
- Name   : Venu
- GitHub : [@Venu-exe](https://github.com/Venu-exe)
