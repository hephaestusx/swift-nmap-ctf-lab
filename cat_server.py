import socket
import threading

HOST = ''  # Bind to all interfaces
PORT = 9001

cat_art = r"""
  _._     _,-'""`-._
(,-.`._,'(       |\`-/|  <(Meow meow meow meow, meow meow meow.. i'm here to waste company resources... meow)
    `-.-' \ )-`( , o o)
          `-    \`_`"'-   Made by the ALMIGHTY Intern Jerry 
"""

def handle_client(conn, addr):
    with conn:
        conn.sendall(cat_art.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Cat server listening on port {PORT}...")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
