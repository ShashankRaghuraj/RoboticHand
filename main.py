import cwiid
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button_delay = 0.1
GPIO.setup(7,GPIO.OUT)a
GPIO.setup(15,GPIO.OUT)
p= GPIO.PWM(7,50)
s= GPIO.PWM(15,50)
p.start(7.5)
s.start(2.5)

print 'Press 1+2 on your Wiimote now...'
wm = cwiid.Wiimote()
time.sleep(1)

wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

wm.led = 1
wm.rumble = 1
time.sleep(1)
wm.rumble = 0
while True:
    buttons = wm.state['buttons']
    if (buttons & cwiid.BTN_A):    
        motionXLeft = (wm.state['acc'][0] < 126)
        motionXRight = (wm.state['acc'][0] > 126)
        if(motionXLeft == True):
            print("left")
            p.ChangeDutyCycle(12.5)
            time.sleep(button_delay)
        if (motionXRight == True):
            print("right")
            p.ChangeDutyCycle(2.5)
            time.sleep(button_delay)    
    if (buttons & cwiid.BTN_B):
        motionUP = (wm.state['acc'][1] < 126)
        motionDOWN = (wm.state['acc'][1] > 126)
        if(motionUP == True):
            print("up")
            s.ChangeDutyCycle(1.5)
            time.sleep(button_delay)
        if (motionDOWN == True):
            print("down")
            s.ChangeDutyCycle(4.5)
            time.sleep(button_delay)
    if (buttons & cwiid.BTN_HOME):
        p.ChangeDutyCycle(7.5)
        time.sleep(button_delay)
        s.ChangeDutyCycle(1.5)
        time.sleep(button_delay)
    if (buttons - cwiid.BTN_A - cwiid.BTN_B == 0):    
        motionXLeft = (wm.state['acc'][0] < 126)
        motionXRight = (wm.state['acc'][0] > 126)
        if(motionXLeft == True):
            print("left")
            p.ChangeDutyCycle(9.5)
            time.sleep(button_delay)
        if (motionXRight == True):
            print("right")
            p.ChangeDutyCycle(5.5)
            time.sleep(button_delay)
        time.sleep(button_delay)
    
