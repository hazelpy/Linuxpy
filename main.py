import sys
import os

from os import system as System

__readme__ = """\
This is my first Linux application!
Using Python 3, I wrote this code myself. \
"""

def Clear():
    clearname = "clear"

    if os.name == "nt":
        clearname = "cls"

    System(clearname)

def ReadMe():
    print(__readme__)

def Version():
    print("Linuxpy v0.0.1")

def _end():
    print("Usage: python3 main.py [-v | -readme | -clear]")
    sys.exit(0)

enum = {"-readme": ReadMe, "-v": Version, "-clear": Clear}

if not len(sys.argv) > 1: _end()
if sys.argv[1] in enum.keys():
    enum[sys.argv[1]]()
