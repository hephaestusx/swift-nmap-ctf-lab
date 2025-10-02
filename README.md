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
