import subprocess
import glob
import os
def WATCH():
    # detox: remove all spaces from filenames Linux: apt install detox
    #PYTHON3 use: subprocess.run(["detox", "/home/jack/Downloads"])
    THIS_dir = os.getcwd()
    subprocess.call(["detox", THIS_dir])
    list_of_files = glob.glob(THIS_dir+"/*.mp4") # * means all if need specific format then *.csv
    src = max(list_of_files, key=os.path.getctime)
    bashCommand ="vlc --preferred-resolution 240 "+src 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate() 
    return 
