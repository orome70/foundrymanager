# This file is intended to perform the first tests.

# 1 we need to be able to launch and monitor processes. 
#   Popen is the right tool: it encapsulates a process and is able to check on it as often as necessary.

import subprocess
import time

# Create a process

## Python 3.10 permits to have a "user argument". Not available in python 3.8.
## procTest = subprocess.Popen(["emacs"],user="kris")
try:
    procTest = subprocess.Popen(["emacs"])
except OSError:
    print("Launch error\n") 

while True:
    time.sleep(0.5)
    if procTest.poll()!= None : 
        print("The end\n")        
        exit(0)

