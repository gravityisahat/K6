#!/usr/bin/python
"""
List available PortMidi ports.
"""

from __future__ import print_function

import os
import sys
import mido
import os



inport =mido.open_input ('Scarlett 2i4 USB MIDI 1')
msg = inport.receive()

for msg in inport:
   print("the message type is %s" %msg.type)
   X = str(msg.type)
   Y = str('note_on')
   print(X)
   print(Y)
   if X == Y:
        os.system('sudo /var/lib/asterisk/scripts/ringbash.sh')
        print('ring')
exit()


        
