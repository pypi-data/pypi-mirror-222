import os
import subprocess
import sys

from libs.in_win import inside_windows

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
exec = sys.executable
print(exec)
if inside_windows():
    exec = exec.replace("python.exe", "pythonw.exe")
    subprocess.run([exec, "v2rayp.py"])
    exit()
else:
    subprocess.run([exec, "v2rayp.py"])
#####
