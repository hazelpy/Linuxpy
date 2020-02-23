import sys
import os
import listattr as List

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

def Version(debug):
    if not debug: print("Linuxpy v0.0.1")
    return 0.01

def _end():
    print(f"Linuxpy v{Version(True)} - Made by Hazelpy")
    print("Usage: python3 main.py [-v | -readme | -clear]")
    sys.exit(0)

def Pow():
    if len(sys.argv) > 3:
        print(List.Pow([float(sys.argv[2])], float(sys.argv[3]))[0])

def Test():
    if not len(sys.argv) > 2: print(List.Half([1, 2, 3, 4, 5]))
    else:
        toggle = False

        if sys.argv[2] == "True":
            toggle = True

        print(List.Half([1, 2, 3, 4, 5], toggle))

enum = {"-readme": ReadMe, "-v": Version, "-clear": Clear, "--pow": Pow, "--test": Test}

if not len(sys.argv) > 1: _end()
if sys.argv[1] in enum.keys():
    enum[sys.argv[1]]()
