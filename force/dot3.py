#!/usr/bin/env python

import dothat.lcd as l
import dothat.backlight as b
import signal
import os
from time import sleep
import sys
import math

"""
Captouch provides the @captouch.on() decorator
to make it super easy to attach handlers to each button.

It's also a drop-in replacement for joystick, with one exception:
it has a "cancel" method.

The handler will receive "channel" ( corresponding to a particular
button ID ) and "event" ( corresponding to press/release ) arguments.
"""

def pid_is_running(pid):
    """
    Return pid if pid is still going.

    >>> import os
    >>> mypid = os.getpid()
    >>> mypid == pid_is_running(mypid)
    True
    >>> pid_is_running(1000000) is None
    True
    """

    try:
        os.kill(pid, 0)

    except OSError:
        return

    else:
        return pid

def write_pidfile_or_die(path_to_pidfile):

    if os.path.exists(path_to_pidfile):
        pid = int(open(path_to_pidfile).read())

        if pid_is_running(pid):
            print("Sorry, found a pidfile!  Process {0} is still running.".format(pid))
	    os.kill(pid, signal.SIGKILL)

        else:
            os.remove(path_to_pidfile)

    open(path_to_pidfile, 'w').write(str(os.getpid()))
    return path_to_pidfile

def dark_side():
  print("Dark side of the force!")
  l.clear()
  b.rgb(255,0,0)
  l.write("Dark side of the force!")
  sleep(10)
  test()

def light_side():
  print("Light side of the force!")
  l.clear()
  b.rgb(0,0,255)
  l.write("Light side of the force!")
  sleep(10)
  test()

def test():
  print("Testing")
  l.clear()
  l.write("Dark or light side of the force?")
  x = 0

  while True:
    	x+=1

    	b.sweep( (x%360)/360.0)
    	sleep(0.01)

# Prevent the script exiting!

if __name__ == '__main__':

	write_pidfile_or_die('/tmp/dot3.pid')
	print sys.argv
	if sys.argv[1] == "Light":
		light_side()
	if sys.argv[1] == "Dark":
		dark_side()
	else:
		print "These are not the droids you are looking for"
		test()
	
	print('process {0} finished work!'.format(os.getpid()))
	signal.pause()
