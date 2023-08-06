import os, sys
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
subprocess.run([sys.executable, "v2rayp.py"])
#####
