#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.tools import wait, StopWatch, DataLog

ev3 = EV3Brick()
lever = Motor(Port.D)
button = TouchSensor(Port.S1)
IRsensor = InfraredSensor(Port.S4)


from time import sleep
import math

import os

# before start:
# - start multimidicast [&]
# - ensure midipipe exists - mkfifo midipipe
# - start amidicat - ./amidicat --port 128:0 --hex < ./midipipe


# check if multimidicast is running and start it if not
if os.popen('pgrep multimidicast').read().strip() == '':
    os.system('./multimidicast &')
    print('multimidicast started')
else:
    print('multidicast was running')

wait(500)

# check if midipipe was created
if os.popen('ls midipipe').read().strip() == 'midipipe':
    print('midipipe exists')
else:
    os.system('mkfifo midipipe')
    print('midipipe created')

# check if amidicat is running and start it if not
print(os.popen('pgrep amidicat').read().strip())

if os.popen('pgrep amidicat').read().strip() == '':
    os.system('./amidicat --port 128:0 --hex < ./midipipe &')
    print('amidicat started')
else:
    print('amidicat was running')

print(os.popen('pgrep amidicat').read().strip())


volume = 70

## Add things about keys and what notes apply to what

from midi_notes import majors, minors, bluemajors, blueminors

SCALES = [majors, minors, bluemajors, blueminors]

scale_type = 0
scale_key = 0
octave = 3

scale_up = False
scale_down = False
key_up = False
key_down = False
octave_up = False
octave_down = False

lever.run_until_stalled(50,then=Stop.BRAKE,duty_limit=None)
lever.run_angle(50,-30,then=stop.HOLD,wait=True)
lever.reset_angle(0)
bend = 0

play = False

ev3.light.on(Colour.GREEN)

def getFret:
    fret = math.ceil(dist/10) - ## add minimum distance to get fret 0, 1, 2 etc...
    return fret

def changePars:
    if LEFT in buttons.pressed() and octave_up = False:
        octave = octave + 1
        octave_up = True
    elif LEFT not in buttons.pressed():
        octave_up = False

    if RIGHT in buttons.pressed() and octave_down = False:
        octave = octave - 1
        octave_down = True
    elif RIGHT not in buttons.pressed():
        octave_down = False

    if DOWN in buttons.pressed() and key_up = False:
        scale_key = scale_key + 1
        key_up = True
    elif DOWN not in buttons.pressed():
        key_up = False

    if UP in buttons.pressed() and key_down = False:
        scale_key = scale_key - 1
        key_down = True
    elif UP not in buttons.pressed():
        key_down = False

        

while True:

    changePars()    
    
    current = SCALES[scale_type][scale_key] # sets the current scale
    
    bend = lever.angle() # gets the current pitch bend lever position

    if bend < -5 or bend > 5:
        ## add the pitch bend midi code

    note1 = None
    note2 = None

    dist = IRsensor.distance()

    
    # code that senses a fret change whilst playing

    changed = False

    fret = getFret()
    note1 = current.notes[fret + (octave*current.octave)]
    wait(10)
    fret = getFret()
    note2 = current.notes[fret + (octave*current.octave)]

    if note1 != note2:
        changed = True


    # Code that plays a note when the button is pressed,
    #   or changes the note if the fret changes
    
    if button.pressed():

        if play == False:

            ## send midi note on
            play = True

        elif play == True and changed == True:

            ## another midi note on, old midi note off

    else:

        ## send midi notes all off


        
    
