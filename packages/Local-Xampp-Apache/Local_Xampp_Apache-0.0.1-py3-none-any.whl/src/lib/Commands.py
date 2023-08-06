
import subprocess
import time
import psutil
import os
class Commands:
    def __init__(self):
        self.xampp_apache_path = "C:/xampp/apache/bin/httpd.exe"

    
    def run_batch_file(self):
        try:
            subprocess.Popen(self.xampp_apache_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
            print("Started...")
        except Exception as e:
            print("Error: ", e)

    def is_apache_running(self):
        try:
            subprocess.run([self.xampp_apache_path, "-t"], check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def kill_apache(self):
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == os.path.basename(self.xampp_apache_path):
                    proc.kill()
                    print("Apache server has been stopped successfully.")
                    break
            else:
                print("Apache process not found. Nothing to stop.")
        except Exception as e:
            print("Error:", e)

