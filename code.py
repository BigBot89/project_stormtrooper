import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

buttonRecordPin = board.GP15
buttonLastFivePin = board.GP14
buttonCapturePin = board.GP13
#buttonFpsPin = board.GP12
buttonLoadStatePin = board.GP12
buttonSaveStatePin = board.GP11

ledPinOB = board.GP25
ledPin = board.GP16

keyboard = Keyboard(usb_hid.devices)

buttonRecord = digitalio.DigitalInOut(buttonRecordPin)
buttonRecord.direction = digitalio.Direction.INPUT
buttonRecord.pull = digitalio.Pull.DOWN

buttonLastFive = digitalio.DigitalInOut(buttonLastFivePin)
buttonLastFive.direction = digitalio.Direction.INPUT
buttonLastFive.pull = digitalio.Pull.DOWN

buttonCapture = digitalio.DigitalInOut(buttonCapturePin)
buttonCapture.direction = digitalio.Direction.INPUT
buttonCapture.pull = digitalio.Pull.DOWN

#buttonFps = digitalio.DigitalInOut(buttonFpsPin)
#buttonFps.direction = digitalio.Direction.INPUT
#buttonFps.pull = digitalio.Pull.DOWN

buttonLS = digitalio.DigitalInOut(buttonLoadStatePin)
buttonLS.direction = digitalio.Direction.INPUT
buttonLS.pull = digitalio.Pull.DOWN

buttonSS = digitalio.DigitalInOut(buttonSaveStatePin)
buttonSS.direction = digitalio.Direction.INPUT
buttonSS.pull = digitalio.Pull.DOWN

ledOB = digitalio.DigitalInOut(ledPinOB)
ledOB.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(ledPin)
led.direction = digitalio.Direction.OUTPUT

while True:
    ledOB.value = False
    led.value = False
    pressCount = 0
    if buttonRecord.value == True and buttonCapture.value == True:
        print("Both were pressed simultaneously. Ignore")
    else:
        while buttonRecord.value == True:
            ledOB.value = True
            led.value = True
            if pressCount < 1:
                keyboard.press(Keycode.ALT, Keycode.F9)
                print("'Record' button was pressed")
                time.sleep(0.1)
                keyboard.release(Keycode.ALT, Keycode.F9)
                print("'Record' button was released")
                pressCount = pressCount + 1
                time.sleep(0.5)
        while buttonLastFive.value == True:
            ledOB.value = True
            led.value = True
            if pressCount < 1:
                keyboard.press(Keycode.ALT, Keycode.F10)
                print("'LastFive' button was pressed")
                time.sleep(0.1)
                keyboard.release(Keycode.ALT, Keycode.F10)
                print("'LastFive' button was released")
                pressCount = pressCount + 1
                time.sleep(0.5)
        while buttonCapture.value == True:
            ledOB.value = True
            led.value = True
            if pressCount < 1:
                keyboard.press(Keycode.ALT, Keycode.F1)
                print("'Capture' button was pressed")
                time.sleep(0.1)
                keyboard.release(Keycode.ALT, Keycode.F1)
                print("'Capture' button was released")
                pressCount = pressCount + 1
                time.sleep(0.5)
        while buttonLS.value == True:
            ledOB.value = True
            led.value = True
            if pressCount < 1:
                keyboard.press(Keycode.SHIFT, Keycode.F3)
                print("'Load State' button was pressed")
                time.sleep(0.1)
                keyboard.release(Keycode.SHIFT, Keycode.F3)
                print("'Load State' button was released")
                pressCount = pressCount + 1
                time.sleep(0.5)
        while buttonSS.value == True:
            ledOB.value = True
            led.value = True
            if pressCount < 1:
                keyboard.press(Keycode.SHIFT, Keycode.F2)
                print("'Save State' button was pressed")
                time.sleep(0.1)
                keyboard.release(Keycode.SHIFT, Keycode.F2)
                print("'Save State' button was released")
                pressCount = pressCount + 1
                time.sleep(0.5)
            #
        #
    #
#