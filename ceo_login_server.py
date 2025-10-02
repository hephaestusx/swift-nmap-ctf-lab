import socket
import threading

HOST = ''
PORT = 5555

CEO_USERNAME = "big_brother"
CEO_PASSWORD = "passw0rd!"

welcome_msg = "Welcome to BlindEye Solutions CEO Portal\n"
username_prompt = "Username: "
password_prompt = "Password: "
success_msg = """\
Access granted. Welcome, CEO.

Here is your confidential dashboard:
- Revenue: $10M
- Employees: 42
- Security Status: Critical

Congratulations! You’ve successfully accessed the CEO account.
Please submit the username, password, and used ports to the Google form to officially complete the CTF at:
https://forms.gle/u4z8o7Srvm1rSrx7A

Thank you for playing! -Matthew(autumn)
"""
fail_msg = "Access denied. Invalid credentials. Try again.\n"

def recv_line(conn):
    buffer = b""
    while True:
        data = conn.recv(1)
        if not data or data == b"\n":
            break
        buffer += data
    return buffer.decode().strip()

def handle_client(conn, addr):
    with conn:
        conn.sendall(welcome_msg.encode())
        while True:
            conn.sendall(username_prompt.encode())
            username = recv_line(conn)
            if not username:
                break  # Client disconnected
            conn.sendall(password_prompt.encode())
            password = recv_line(conn)
            if not password:
                break  # Client disconnected
            if username == CEO_USERNAME and password == CEO_PASSWORD:
                conn.sendall(success_msg.encode())
                break
            else:
                conn.sendall(fail_msg.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"CEO login server listening on port {PORT}...")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
