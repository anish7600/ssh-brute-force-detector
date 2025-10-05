#!/usr/bin/env python3

import re
import subprocess
from collections import defaultdict

# Brute-force detection threshold
THRESHOLD = 5

# Regex pattern to extract failed login attempts
FAILED_LOGIN_PATTERN = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

def monitor_logs():
    """ Continuously monitors macOS SSH logs in real-time """
    cmd = ["log", "stream", "--predicate", 'process == "sshd"', "--info"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    failed_attempts = defaultdict(int)

    try:
        for line in process.stdout:
            match = re.search(FAILED_LOGIN_PATTERN, line)
            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

                print(f"[ALERT] Failed login from {ip} ({failed_attempts[ip]} attempts)")

                if failed_attempts[ip] >= THRESHOLD:
                    print(f"[WARNING] Potential brute-force attack detected from {ip}")
                    quit()

    except KeyboardInterrupt:
        print("\nStopping SSH log monitoring...")
        process.terminate()

if __name__ == "__main__":
    print("Monitoring SSH logs in real-time on macOS... Press Ctrl+C to stop.")
    monitor_logs()
