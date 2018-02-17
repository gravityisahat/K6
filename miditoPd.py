#!usr/bin/python
import sys
from mido import open_output
from mido import Message
trigger = int(sys.argv[1])
msg = Message('note_on', note=trigger)
outport = open_output()
outport.send(msg)
