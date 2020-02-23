import sys
import os

def Pow(li: list, power):
    re = []

    for item in li:
        re.append(pow(item, power))

    return re

