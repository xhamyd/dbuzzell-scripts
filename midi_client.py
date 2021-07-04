# pip install mido python-rtmidi
import mido
import random
import re


def select_device(device_regex, mode):
    if mode == "in":
        names = mido.get_input_names()
    elif mode == "out":
        names = mido.get_output_names()

    for name in names:
        if re.match(device_regex, name):
            print(f"Selected {name} for {mode}put")
            return name


LAUNCHPAD_REGEX = r"^Launchpad MK2.*$"
input_name = select_device(LAUNCHPAD_REGEX, "in")
output_name = select_device(LAUNCHPAD_REGEX, "out")

with mido.open_input(input_name) as inport, \
        mido.open_output(output_name) as outport, \
        mido.sockets.connect('192.168.1.56', 8080) as midi_server:
    print("MIDI loopback enabled")
    # midi_server.send(mido.Message(type="note_on"))
    while True:
        msg = inport.receive()

        if hasattr(msg, 'velocity') and msg.velocity > 0:
            msg = msg.copy(velocity=random.randint(1, 127))
        elif hasattr(msg, 'value') and msg.value > 0:
            msg = msg.copy(value=random.randint(1, 127))

        print(msg)
        if msg:
            outport.send(msg)
            for _ in range(2):
                midi_server.send(msg)
