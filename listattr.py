import sys
import os

def Pow(li: list, power):
    re = []

    for item in li:
        re.append(pow(item, power))

    return re

def Half(li: list, right = False):
    if right: return [li[i] for i in range(len(li)) if i >= int(len(li) / 2)]
    else: return [li[i] for i in range(len(li)) if i <= int(len(li) / 2)]
