import os
import time
import subprocess

folder_path = 'C:\path\to\folder'

def check_choco_installation():
    try:
        subprocess.run(['choco', '-version'], check=True, shell=True)
    except subprocess.CalledProcessError:
        subprocess.run(['powershell', 'Set-ExecutionPolicy', 'Bypass', '-Scope', 'Process', '-Force'], shell=True)
        subprocess.run(['powershell', 'iex', '(new-object', 'net.webclient).downloadstring(\'https://chocolatey.org/install.ps1\')'], shell=True)

def check_ffmpeg_installation():
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, shell=True)
    except subprocess.CalledProcessError:
        subprocess.run(['choco', 'install', 'ffmpeg'], shell=True)

check_choco_installation()
check_ffmpeg_installation()

while True:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.av1'):
                file_path = os.path.join(root, file)
                output_path = os.path.splitext(file_path)[0] + '.mkv'
                subprocess.run(['ffmpeg', '-i', file_path, '-c:v', 'libx265', '-c:a', 'copy', output_path], shell=True)
                if os.path.exists(output_path):
                    os.remove(file_path)
    time.sleep(28800) # 8 hours
