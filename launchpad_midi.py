import mido
import re
import random

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

    print(names)
    for name in names:
        if re.match(device_regex, name):
            print(f"Selected {name}")
            return name


LAUNCHPAD_REGEX = r"^Launchpad MK2.*$"
input_name = select_device(LAUNCHPAD_REGEX, "in")
output_name = select_device(LAUNCHPAD_REGEX, "out")

with mido.open_input(input_name) as inport, mido.open_output(output_name) as outport:
    while True:
        # msg = inport.receive()
        # Manual is one-indexed, mido is zero indexed
        # Channel 1: on
        # Channel 2: flashing
        # Channel 3: pulsing
        msg = inport.receive()
        print(msg)

        if hasattr(msg, 'velocity') and msg.velocity > 0:
            msg = msg.copy(velocity=random.randint(1, 127))
        elif hasattr(msg, 'value') and msg.value > 0:
            msg = msg.copy(value=random.randint(1, 127))
        outport.send(msg)
