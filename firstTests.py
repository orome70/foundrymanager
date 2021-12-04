# This file is intended to perform the first tests.

# 1 we need to be able to launch and monitor processes. 
#   Popen is the right tool: it encapsulates a process and is able to check on it as often as necessary.

#Foundry launch : node resources/app/main.js --port=30000 --dataPath=/home/kris/foundry_data/
#node /home/kris/foundry/foundry_vtt/resources/app/main.js --dataPath=/home/kris/foundry/foundry_data/ --port=30000

import subprocess
import time

# Create a process

user = "kris"
foundryJs = "/home/kris/foundry/foundry_vtt/resources/app/main.js"
foundryData = "/home/kris/foundry/foundry_data/"
foundryPort = "30000"

## Python 3.10 permits to have a "user argument". Not available in python 3.8.
## procTest = subprocess.Popen(["emacs"],user="kris")

portOption = "--port=" + foundryPort
dataOption = "--dataPath=" + foundryData

try:
    procTest = subprocess.Popen(["node", foundryJs, portOption, dataOption])
except OSError:
    print("Launch error\n") 

while True:
    time.sleep(0.5)
    if procTest.poll()!= None : 
        print("The end\n")        
        exit(0)

