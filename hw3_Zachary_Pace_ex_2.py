'''
Homework 3-2
Name: Zachary Pace
Date: 2/22/2023
Description: Counting all letters present in a sting
'''

import pprint

strInput = str(input("Input String: "))
charDict = {}

for i in range(len(strInput)):
    # checks if letter is in dictionary already
    if strInput[i] not in charDict:
        charDict[strInput[i]] = 1
    else:
        charDict[strInput[i]] += 1

pprint.pprint(charDict)
