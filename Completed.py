#!/user/bin/python
import os
import sys
from time import sleep
import glob
def track_download():
    list_of_files = glob.glob(os.getcwd()+'/Downloads/*') # * means all if need specific format then *.csv
    src = max(list_of_files, key=os.path.getctime)
    TEXT=[]
    while True:
        file1 = os.stat(src) # initial file size
        file1_size = file1.st_size
        num=file1_size*.000001
        sys.stdout.write("%.2f" % num)
        sys.stdout.write("Mb ")
        #sys.stdout.write(file1_size),"Mb  ")
        sys.stdout.flush()
        # your script here that collects and writes data (increase file size)
        #print("%.2f" % file1_size),"Mb  ",
        sleep(20)
        file2 = os.stat(src) # updated file size

        file2_size = file2.st_size
        comp = file2_size - file1_size # compares sizes
        if comp == 0:
            #restart_program(src)
            TEXT.append("The File Appears to be completed.")
            print ("Waited 40 seconds No filesize change")
            break
        else:
            sleep(20)
    return TEXT
