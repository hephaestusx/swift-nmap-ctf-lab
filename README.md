# swift-nmap-ctf-lab
SWIFT NMAP Workshop, for october 3rd, 2025


## E BOARD / SWINTERN USAGE ONLY 2025

Instructions:

Pre-Requisites: you should have a clean ubuntu LTS 22.04 server install, ready to go updated and upgraded WITH openssh already installed and scripts done if you have already done steps 1 and 2 (e.g you just duplicated that server once you made sure everything was running properly which would be fine)

1. Create directory for /home/nmaplab (mkdir /home/nmaplab) 

2. Copy all files with wget and pastebin (original python script also included on the repo should it be needed) onto the server in the directory using pastebinit (The order should go cat_server.py, ceo_login_server.py, README_server.py, sql_dump_server.py start_all_servers.py

3. (optional if dir already there), but mkdir /etc/systemd/service for the systemd script which the dir SHOULD be there

4. add user ctfplayer1-30, e.g ctfplayer1, ctfplayer2, ctfplayer3 with locked down privs:

   - sudo useradd -m -s /bin/bash ctfplayer(1-30) && sudo passwd -e ctfplayer(1-30)
   - sudo usermod -G "" ctfplayer(1-30)
   *the (1-30) would be in place of actual numbers like: 1,2,3

6. ssh in, confirm access to all scripts, e.g doing nc 1337,9001,4444,5555 make sure no sudo su and done

# how everything works together

the NMAP lab is comprised of 4 parts:

Port 1337, aka the "message port"
Port 9001, deception port
port 4444, database port
port 5555, the login page

all of these are fundamentally build on python but the idea essentially is:

   - The host is left blank to bind to all interfaces and the port is defined
   - the contents are left inside

     whenever somebody tries to SSH in via NC(netcat) at the ip and port, the python script accepts the connection via the connection and address and displays content:

included in the document is a template for c++ and go, but you could also get away with just using python solely, 

TO RUN FOR C++

g++ -std=c++17 -pthread readme_server.cpp -o readme_server
./readme_server\

nc 192.168.1.x 1234


TO RUN FOR GOLANG:

go build -o readme_server readme_server.go
./readme_server

nc 192.168.1.x 1234


