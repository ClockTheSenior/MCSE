from asyncio.base_futures import _FINISHED
import json, os, platform, shutil, time, sys
from distutils.core import setup
import codecs
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'UTF-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

print("\033[1;32;40m███╗   ███╗ ██████╗███████╗███████╗ \n████╗ ████║██╔════╝██╔════╝██╔════╝ \n██╔████╔██║██║     ███████╗█████╗  \n██║╚██╔╝██║██║     ╚════██║██╔══╝ \n██║ ╚═╝ ██║╚██████╗███████║███████╗ \n╚═╝     ╚═╝ ╚═════╝╚══════╝╚══════╝")
print("\033[0;37;45m Made by ClockTheSenior \033[0;37;40m \n")

''' 
     Copies audio files from indescript hashed folders to named sorted folders.
     You may need to change output path.
 '''
 
 # This section should work on any system as well
print("\033[1;33;40mWe have detected that you are running " + platform.system(),"!")
if platform.system() == "Windows":
     MC_ASSETS = os.path.expandvars(r"%APPDATA%/.minecraft/assets")
else:
     MC_ASSETS = os.path.expanduser(r"~/.minecraft/assets")

print("\033[1;34;40mEnter the the version to get the sounds from (has to be installed)")
MC_INPUTVERSION = input("\033[1;37;40m")
print(LINE_UP, end=LINE_CLEAR)
print(LINE_UP, end=LINE_CLEAR)
 # Find the latest installed version of minecraft (choose the last element in assets/indexes)
if platform.system() == "Windows":
     MC_VERSION = os.path.expandvars("%APPDATA%/.minecraft/assets/indexers/"+MC_INPUTVERSION+".json")
else:
     MC_VERSION = os.path.expanduser("~/.minecraft/assets/indexers/"+MC_INPUTVERSION+".json")

 # Change this if you want to put the sound files somewhere else
print("\033[1;34;40mEnter the path that you want to extract the sounds to:")
OUTPUT_PATH = os.path.normpath(os.path.expandvars(os.path.expanduser(input("\033[1;37;40m"))))

 
 # Asking for Super Mode
SuperMode = None
print(LINE_UP, end=LINE_CLEAR)
print(LINE_UP, end=LINE_CLEAR)
while SuperMode not in ("Enabled", "Disabled"):
     print("\033[1;34;40mBefore we proceed, would you like to enable Super Mode? (Y/n)")
     SuperMode = input("\033[1;37;40m")
     print(LINE_UP, end=LINE_CLEAR)
     print(LINE_UP, end=LINE_CLEAR)
     if SuperMode == ("Y"):
          SuperMode = "Enabled"
     elif SuperMode == ("n"):
          SuperMode = "Disabled"

     if SuperMode == ("N"):
          SuperMode = "Disabled"
     elif SuperMode == ("y"):
          SuperMode = "Enabled"

     if SuperMode == ("Disabled"):
          ExtractionSpeed = 0.05
     elif SuperMode == "Enabled":
          ExtractionSpeed = 0


 # These are unlikely to change
MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_INPUTVERSION}.json"
MC_OBJECTS_PATH = f"{MC_ASSETS}/objects"
MC_SOUNDS = r"minecraft/sounds/"

with open(MC_OBJECT_INDEX, "r") as read_file:
     # Parse the JSON file into a dictionary
     data = json.load(read_file)
 
     # Find each line with MC_SOUNDS prefix, remove the prefix and keep the rest of the path and the hash
     sounds = {k[len(MC_SOUNDS):] : v["hash"] for (k, v) in data["objects"].items() if k.startswith(MC_SOUNDS)}
     
     print("You can exit/cancel with Ctrl + C")
     print("\033[1;36;40mCurrent File:")
     for fpath, fhash in sounds.items():
         # Ensure the paths are good to go for Windows with properly escaped backslashes in the string
         src_fpath = os.path.normpath(f"{MC_OBJECTS_PATH}/{fhash[:2]}/{fhash}")
         dest_fpath = os.path.normpath(f"{OUTPUT_PATH}/sounds/{fpath}")
 
         # Print current extracted file
         try:
               loop = range(1, len(fpath) + 1)
               for i in reversed(loop):
                         print("\033[2;37;40m", fpath)
                         time.sleep(ExtractionSpeed)
                         print(LINE_UP, end=LINE_CLEAR)
                         
                         
         except KeyboardInterrupt:
                    print(LINE_UP, end=LINE_CLEAR)
                    print(LINE_UP, end=LINE_CLEAR)
                    print("\033[1;31;40mClosing!")
                    time.sleep(1)
                    raise SystemExit
          
               

         # Make any directories needed to put the output file into as Python expects
         os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)

         # Copy the file
         shutil.copyfile(src_fpath, dest_fpath)
         
print("\033[1;32;40mDone!")
time.sleep(5)
print("\033[1;31;40mClosing!")
time.sleep(3)
print(LINE_UP, end=LINE_CLEAR)
print(LINE_UP, end=LINE_CLEAR)
print(LINE_UP, end=LINE_CLEAR)
print(LINE_UP, end=LINE_CLEAR)
time.sleep(2)
raise SystemExit
