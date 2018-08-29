#!/usr/bin/python
#Pause/play
import os

fname = PauseFile.txt

if os.path.exists(fname):#If PauseFile exists, nuke it
    os.remove(fname)
else:#If PauseFile doesn't exist, make it
    f = open(fname, "w")
    f.close()
