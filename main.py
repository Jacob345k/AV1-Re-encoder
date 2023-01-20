import subprocess
import time

# Specify the executable files and process names here
# The process name is the name that appears in the task manager
# These must have the same number of elements

EXE_NAMES = ["program1.exe", "program2.exe"]
PROCESS_NAMES = ["program1.exe", "program2.exe"]

# Specify the time to wait before killing the process in seconds
WAIT_TIME = 300

for exe, process in zip(EXE_NAMES,PROCESS_NAMES):
    # Run the executable file
    subprocess.Popen(exe)

    # Wait for the specified time
    time.sleep(WAIT_TIME)

    # Kill the executable file process
    subprocess.Popen(f"taskkill /f /im {process}")
