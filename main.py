import os
import time
import subprocess
import tempfile

folder_path = 'C:\path\to\folder'

def check_choco_installation():
    try:
        subprocess.run(['choco', '-version'], check=True)
    except:
        subprocess.run(['powershell', 'Set-ExecutionPolicy', 'Bypass', '-Scope', 'Process', '-Force'], shell=True)
        subprocess.run(['powershell', 'iex', '(new-object', 'net.webclient).downloadstring(\'https://chocolatey.org/install.ps1\')'], shell=True)
    subprocess.run(['choco', 'install', 'ffmpeg'], shell=True)

check_choco_installation()
time_of_check = time.time()

while True:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.av1'):
                file_path = os.path.join(root, file)
                output_path = os.path.splitext(file_path)[0].replace('.av1','') + '.mkv'
                temp_dir = tempfile.mkdtemp()
                subprocess.run(['ffmpeg', '-i', file_path, '-c:v', 'libx265', '-c:a', 'copy', '-threads','4', os.path.join(temp_dir,output_path)], shell=True)
                if os.path.exists(os.path.join(temp_dir,output_path)):
                    os.remove(file_path)
                    os.rename(os.path.join(temp_dir,output_path),file_path)
                    os.rmdir(temp_dir)
    time.sleep(172800) # wait 2 days