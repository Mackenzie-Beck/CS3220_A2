from MazeMapData import *
import random

mazeWorldStates = [coord for coord in mazeLocations]

agentFacing = ['North', 'East', 'South', 'West']

keyList = [(coord,direction) for coord in mazeLocations for direction in agentFacing]

