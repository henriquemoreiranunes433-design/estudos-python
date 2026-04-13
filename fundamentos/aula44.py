import subprocess
import sys

print(sys.platform)

cmd = ['ping', '127.0.0.1']

proc = subprocess.run(
    cmd, capture_output= True
)

print(proc.stdout.decode('cp850'))