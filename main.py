import sys

__readme__ = """\
This is my first Linux application!
Using Python 3, I wrote this code myself. \
"""

def ReadMe():
    print(__readme__)

def Version():
    print("Linuxpy v0.0.1")

enum = {"-readme": ReadMe, "-v": Version}

if not len(sys.argv) > 1: sys.exit(0)
if sys.argv[1] in enum.keys():
    enum[sys.argv[1]]()
