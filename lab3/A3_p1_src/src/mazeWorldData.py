from MazeMapData import *
import random

keyList = [state for state in mazeData.keys()]

agentAction = ['Left', 'Advance', 'Right']

result = []

def makeData():
    d1 = {}
    for i in range(len(keyList)):
        d1[keyList[i]] = mazeData[keyList[i]]
    return d1

def mazeStateLocations():
    return mazeLocations