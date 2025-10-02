import socket
import threading

HOST = ''  # Bind to all interfaces
PORT = 4444

fake_sql_dump = """\
-- BlindEye Solutions: SQLDB_V.1 Employee Database Dump --
+----+----------------+------------+---------------------+----------------+
| ID | Username       | Role       | Last Login          | Password       |
+----+----------------+------------+---------------------+----------------+
| 1  | big_brother    | CEO        | 2025-08-09 14:22:10 | passw0rd!      |
| 2  | jerry          | Intern     | 2025-08-10 09:15:45 | letme1npls     |
| 3  | bob            | Developer  | 2025-08-10 08:05:12 | devpa5s        |
| 4  | larry          | Sysadmin   | 2025-08-09 20:33:55 | larrytheGOAT   |
+----+----------------+------------+---------------------+----------------+

*Note: Passwords are stored in plaintext due to "legacy reasons." (P.S also our software just sucks tbh we need a budget
increase for this kinda stuff -larry)
"""

def handle_client(conn, addr):
    with conn:
        conn.sendall(fake_sql_dump.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Fake SQL dump server listening on port {PORT}...")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
