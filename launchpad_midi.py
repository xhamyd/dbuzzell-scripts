"""
Setup instructions:
    1. python3 on RPi
    2. sudo apt install sense-hat
    3. pip3 install mido python-rtmidi recordclass
    4. python3 launchpad_midi.py

"""
import mido
import platform
import re
import random
from sense_hat import SenseHat

from launchpad_colors import LAUNCHPAD_COLORS

assert platform.python_version_tuple() > ('3', '6', '0')

"""
Midi Through:Midi Through Port-0 14:0
Launchpad MK2:Launchpad MK2 MIDI 1 20:0
Midi Through:Midi Through Port-0 14:0
Launchpad MK2:Launchpad MK2 MIDI 1 20:0
"""

def select_device(device_regex, mode):
    if mode == "in":
        names = mido.get_input_names()
    elif mode == "out":
        names = mido.get_output_names()

    for name in names:
        if re.match(device_regex, name):
            print(f"Selected {name} for {mode}put")
            return name

# Initialize the SenseHat
sense = SenseHat()
sense.clear()
sense.set_rotation(0)  # HDMI port facing down
sense.low_light = True

LAUNCHPAD_REGEX = r"^Launchpad MK2.*$"
input_name = select_device(LAUNCHPAD_REGEX, "in")
output_name = select_device(LAUNCHPAD_REGEX, "out")

_DEFAULT_MIN_VELCOLOR = 48
MIN_VELCOLOR = _DEFAULT_MIN_VELCOLOR // (2 if sense.low_light else 1)

print("Opening devices...")
with mido.open_input(input_name) as inport, mido.open_output(output_name) as outport:
    print("MIDI Loopback enabled")
    while True:
        # Launchpad documentation is one-indexed, mido is zero indexed
        # Channel 1: on
        # Channel 2: flashing
        # Channel 3: pulsing
        msg = inport.receive()

        if hasattr(msg, 'velocity') and msg.velocity > 0:
            msg = msg.copy(velocity=random.randint(1, 127))
        elif hasattr(msg, 'value') and msg.value > 0:
            msg = msg.copy(value=random.randint(1, 127))

        outport.send(msg)

        if re.match("^note_(?:on|off)$", msg.type):
            #print(msg.note, "on" if msg.velocity > 0 else "off")
            row = 8 - msg.note // 10
            col = msg.note % 10 - 1

            color = LAUNCHPAD_COLORS[msg.velocity]
            color.red = max(color.red, MIN_VELCOLOR) if color.red > 0 else 0
            color.green = max(color.green, MIN_VELCOLOR) if color.green > 0 else 0
            color.blue = max(color.blue, MIN_VELCOLOR) if color.blue > 0 else 0

            if row in range(0, 8) and col in range(0, 8):  # range is [a, b) inc/exc
                sense.set_pixel(col, row, color)  # x=col, y=row
                print(f"row={row} col={col} color={color}")
