import os
import time
import subprocess

folder_path = 'C:\path\to\folder'
temp_root = 'C:\path\to\temp\folder'

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

# This function checks if chocolatey package manager is installed and installs it if it's not
check_choco_installation()

# This function checks if ffmpeg is installed and installs it if it's not
check_ffmpeg_installation()

time_of_check = time.time()

# This loop checks for .av1 files in the specified folder and its subdirectories
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.av1'):
            file_path = os.path.join(root, file)
            output_path = os.path.splitext(file_path)[0].replace('.av1','') + '.mkv'
            temp_dir = os.path.join(temp_root, file + '_temp')
            os.makedirs(temp_dir, exist_ok=True)
            subprocess.run(['ffmpeg', '-i', file_path, '-c:v', 'libx265', '-c:a', 'copy', '-threads','4', os.path.join(temp_dir,output_path)], shell=True)
            if os.path.exists(os.path.join(temp_dir,output_path)):
                os.remove(file_path)
                os.rename(os.path.join(temp_dir,output_path),file_path)
                os.rmdir(temp_dir)

# This while loop runs indefinitely and checks for .av1 files every 2 days
while True:
    if time.time() - time_of_check > 172800:  # 2 days
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.av1'):
                    file_path = os.path.join(root, file)
                    output_path = os.path.splitext(file_path)[0].replace('.av1','') + '.mkv'
                    temp_dir = os.path.join(temp_root, file + '_temp')
                    os.maked 
