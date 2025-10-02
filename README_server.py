import socket
import threading

HOST = ''  # Bind to all interfaces
PORT = 1337

readme = """\
INTERCEPTED COMMS FROM SYSADMIN -> BLINDEYE SOLUTIONS CYBERTEAM 08/10/25:


FROM SYSADMIN "LARRY"
TITLE: URGENT!! READ ASAP AND HELP A BROTHER OUT!!
BEGIN MESSAGE:

I'll cut to the chase and formalities. Our intern (You know who YOU are) has ONCE AGAIN ruined our infastructure.
Honestly, I don't even know why we hire interns, at this point - incompetent, the lot of them. Anyways, our good 
friend Jerry has decided it was a wonderful idea to open up the Port 1337 to the whole wide internet, so every Joe
Schmoe can access our servers, even as the Sysadmin, I can't close the floodgates now. Moreover, I managed to 
stop the intern from making our SQL server production-ready on port 4444. Our "Prodigy" also decided to poke some fun 
by adding a "cat in the bag" at port 9001 that corrupts logs, and the cherry on top -our CEO still HASN'T. CHANGED.
HIS. PASSWORD. The CEO login page is still running on port 5555. I have no idea how we are still in buisness.
Good luck to this forsaken team, and may the cyber elites save this company.

END MESSAGE.
"""

def handle_client(conn, addr):
    with conn:
        conn.sendall(readme.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"README server listening on port {PORT}...")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
