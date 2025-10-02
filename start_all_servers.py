import subprocess
import time
import os
print("Current working directory:", os.getcwd())

server_scripts = [
    "README_server.py",
    "cat_server.py",
    "sql_dump_server.py",
    "ceo_login_server.py"
]

processes = []

for script in server_scripts:
    print(f"Starting {script}...")
    p = subprocess.Popen(["python3", script])
    processes.append(p)
    time.sleep(1)  # slight delay to stagger startups

print("All servers started. Press Ctrl+C to stop.")

try:
    while True:
        # Keep script running to keep subprocesses alive
        time.sleep(10)
except KeyboardInterrupt:
    print("\nShutting down servers...")
    for p in processes:
        p.terminate()
    print("All servers stopped.")
