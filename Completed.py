import os
from time import sleep
import glob
def restart_program():
    list_of_files = glob.glob('/home/jack/Downloads/*') # * means all if need specific format then *.csv
    src = max(list_of_files, key=os.path.getctime)
    TEXT=[]
    while True:
        file1 = os.stat(src) # initial file size
        file1_size = file1.st_size
        print (file1_size, end=" ")
        # your script here that collects and writes data (increase file size)
        sleep(15)
        file2 = os.stat(src) # updated file size
        file2_size = file2.st_size
        comp = file2_size - file1_size # compares sizes
        if comp == 0:
            #restart_program(src)
            TEXT.append("The File Appears to be completed.")
            print ("No filesize change")
            break
        else:
            sleep(15)
    return TEXT