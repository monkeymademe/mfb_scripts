#!/usr/bin/env python
import skywriter
import signal
import paramiko


some_value = 0
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def send_to_dot3(force):
	if force == "Light":
		cmd_to_execute = 'sudo python /home/pi/mfb_scripts/force/dot3.py Light'
	if force == "Dark":
		cmd_to_execute = 'sudo python /home/pi/mfb_scripts/force/dot3.py Dark'
	ssh.connect("192.168.2.51", username="pi", password="raspberry")
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
	

@skywriter.flick()
def flick(start,finish):
  print('Got a flick!', start, finish)
  if start == "east":
    	#autopy.key.tap(autopy.key.K_LEFT)
	send_to_dot3('Dark')
  if start == "west":
    	#autopy.key.tap(autopy.key.K_RIGHT)
	send_to_dot3('Light')
  if start == "north":
    	#autopy.key.tap(autopy.key.K_DOWN)
  	print start
  if start == "south":
    	#autopy.key.tap(autopy.key.K_UP)
	print start

@skywriter.tap()
def tap(position):
  print "Tap Tap"


signal.pause()
