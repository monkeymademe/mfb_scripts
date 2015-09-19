import time
import RPi.GPIO as io

io.setmode(io.BCM)
 
pir_pin =18
goal_count = 0
  
io.setup(pir_pin, io.IN)# activate input

def goal(goal_count):
	print "SCORE!"
	goal_count = goal_count + 1
	time.sleep(3.0)
  
def take_picture():

while True:
      if io.input(pir_pin):
	goal(goal_count)
      time.sleep(0.5)
