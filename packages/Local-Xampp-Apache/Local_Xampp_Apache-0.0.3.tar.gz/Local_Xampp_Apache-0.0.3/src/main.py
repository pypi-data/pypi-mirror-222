import subprocess
import time
import psutil
import os
import argparse
from src.lib.Commands import Commands

Commands = Commands()

def Apache_start():
    Commands.run_batch_file()

def Is_Apache_run():
    if Commands.is_apache_running():
        print("Apache is Still Runing...")
    else:
        print("Apache is Not Running...")

def Apache_stop():
    Commands.kill_apache()

def main():
    parser = argparse.ArgumentParser(description="Simple Tool to Activate or Stop or Checks the Weather server is Running...")
    
    subparsers = parser.add_subparsers(dest="command", help="Select a command")
    
    Start_apache = subparsers.add_parser("Start", help="Start the Local Apache Xampp Server")
    
    is_apache_running =  subparsers.add_parser("Is_run", help="Check the Local Apache Xampp Server is Running or Not")

    stop_apache = subparsers.add_parser("Stop", help="Stop the Local Apache Xampp Server")

    args = parser.parse_args()

    args = parser.parse_args()
    
    if args.command == "Start":
        Apache_start()
    elif args.command == "Is_run":
        Is_Apache_run()
    elif args.command == "Stop":
        Apache_stop()
    else:
        print("Invalid command. Available commands: Start_Apache,Is_Apache_run,Stop_Apache")


def is_xampp_installed():
    try:
        output = subprocess.check_output("where xampp-control.exe", shell=True, text=True)
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    if is_xampp_installed():
        main()
    else:
        raise Exception("Xampp is Not installed in our System ..\nINstall the Default path of the Xampp")