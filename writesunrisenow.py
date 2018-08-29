#!/usr/bin/python
#writesunrisenow
import datetime

#set next action
f = open("NextAction","w") #open the universal file to write
f.write(str("sunrise")) #write the next action to the file
f.close()

#Set time
g = open("GoTime","w") #open the universal file to write
date_time = str(datetime.datetime.now()) #get datetime
time = date_time.split()[1] #get time
g.write(str(time)) #write the time to the file
g.close() #close the file



