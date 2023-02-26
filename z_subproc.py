import subprocess
import sys

result = subprocess.run(['sshpass', '-panalog', 'scp', '/home/pi/settings.txt', 'root@pluto.local:/www/'])
if result.returncode != 0:
    print('ERROR updating pluto settings.txt')
