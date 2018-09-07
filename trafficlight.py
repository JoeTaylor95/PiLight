#!/usr/bin/python
import RPi.GPIO as G # reference the GPIO library
from time import sleep
import sys, os, time, atexit
from signal import SIGTERM

import shlex
from subprocess import Popen, PIPE
import re

G.setmode(G.BCM)     # use the 'BCM' numbering scheme for the pins
G.setup(21, G.OUT)   # Set pin 18 as an Output
G.setup(16, G.OUT)   # Set pin 18 as an Output
G.setup(20, G.OUT)   # Set pin 18 as an Output

G.output(20, False)
G.output(16, False)
G.output(21, False)

selftest =''

if selftest:
        print "Self Testing"
        #Red    
        G.output(21, True)
        G.output(20, True)
        G.output(16, True)
        sleep(5)
        G.output(21, False)
        G.output(20, False)
        G.output(16, False)
        print "Self Test Complete"

else:
        print "Self Test Turned off"


fpid = os.fork()
if fpid!=0: # Running as daemon now. PID is fpid  

#command = 'curl -XGET https://taylor.am/api/index.php | python -m json.tool'
#p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
#output, err = p.communicate()
#if p.returncode != 0:
        while 1:
                var = 10
                while var == 10:
                        command = 'curl -XGET https://taylor.am/api/index.php | python -m json.tool'
                        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
                        output, err = p.communicate()
                        if p.returncode != 0:
                                print(err)
                        myString = (output.decode("utf-8"))
                        option = re.sub('\s+',' ',myString)
                        #option = (output.decode("utf-8"))
                        print option
                        if p.returncode != 0:
                                result = 0
                        if p.returncode != 1:
                                result = 1
                        if result == '0':
                                print "test 0"
                        if result == 1:
                                print "test 1"
                        G.setmode(G.BCM)     # use the 'BCM' numbering scheme for the pins
                        G.setup(21, G.OUT)   # Set pin 18 as an Output
                        G.setup(16, G.OUT)   # Set pin 18 as an Output
                        G.setup(20, G.OUT)
                        G.output(21, True)
                        sleep(10)
                        G.output(21, False)
                        #Amber
                        G.output(20, True)
                        sleep(1)
                        G.output(20, False)
                        sleep(1)
                        G.output(20, True)
                        sleep(1)
                        G.output(20, False)
                        sleep(1)
                        G.output(20, True)
                        sleep(1)
                        G.output(20, False)
                        sleep(1)
                        G.output(20, True)
                        sleep(1)
                        G.output(20, False)
                        #Green
                        G.output(16, True)
                        sleep(10)
                        #End
                        G.output(20, True)
                        G.output(16, False)
                        sleep(2)
                        G.output(20, False)
                        sleep(2)
                        continue
#sys.exit(0)
#G.cleanup()

