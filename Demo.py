import sys
import os
import time

def DirectoryWatcher(DirName):
    if not os.path.isdir(DirName):
        print("There is no such directory")
        return

    for foldername, subfoldername, filenames in os.walk(DirName):
        for name in filenames:
            print(name)

def main():
    print("________THIS IS AUTOMATION_______")
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        exit()

    if sys.argv[1] in ("--h", "--H"):
        print("This script is used in directory traversal")
        exit()

    if sys.argv[1] in ("--u", "--U"):
        print("Usage of script: ")
        print("python script_name.py directory_name")
        exit()

    try:
        starttime = time.time()
        DirectoryWatcher(sys.argv[1])
        endtime = time.time()
        print("Time required for the script to run: {:.2f} seconds".format(endtime - starttime))
    except Exception as e:
        print("Unable to perform task due to:", e)

if __name__ == "__main__":
    main()
