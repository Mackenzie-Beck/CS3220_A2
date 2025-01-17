import numpy as np
import math
import random
from manhattanDistance import *
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
FIGHT = 4

# Actions dictionary
actions_dict = {
    LEFT: 'left',
    UP: 'up',
    RIGHT: 'right',
    DOWN: 'down',
}

def makeMaze(n,proba_0=0.2,proba_food=0.1):
  size = (n,n)
  # resulting array will have 20% of zeros
  # resulting array will have 10% of food pellets
  arrMaze=np.random.choice([0,1,2], size=size, p=[proba_0, 1-proba_0-proba_food,proba_food])
  ghosts = 0
  while ghosts > 0:
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)
    if (i == 0 and j == 0) or (i == n-1 and j == n-1):
      continue
    if arrMaze[i,j] == 1:
      arrMaze[i,j] = 3
      ghosts -= 1
  return arrMaze


def defineMazeAvailableActions(arr):
  n=arr.shape[0]
  mazeAvailableActions={}
  for i in range(n):
    for j in range(n):
      if i==0 and j==0:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[2],actions_dict[3]])
          if arr[i+1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[3])
          if arr[i,j+1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[2])
      elif i==0 and j==n-1:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[0],actions_dict[3]])
          if arr[i+1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[3])
          if arr[i,j-1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[0])
      elif i==n-1 and j==0:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[1],actions_dict[2]])
          if arr[i-1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[1])
          if arr[i,j+1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[2])
          
      elif i==n-1 and j==n-1:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[0],actions_dict[1]])
          if arr[i-1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[0])
          if arr[i,j-1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[1])
      elif i==0:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[0],actions_dict[2],actions_dict[3]])
          if arr[i,j-1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[0])
          if arr[i,j+1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[2])
          if arr[i+1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[3])
      elif i==n-1:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[0],actions_dict[1],actions_dict[2]])
          if arr[i,j-1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[0])
          if arr[i,j+1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[2])
          if arr[i-1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[1]) 
      elif j==0:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[1],actions_dict[2],actions_dict[3]])
          if arr[i-1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[1]) 
          if arr[i+1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[3])
          if arr[i,j+1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[2])
      elif j==n-1:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[0],actions_dict[1],actions_dict[3]])
          if arr[i,j-1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[0])
          if arr[i-1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[1]) 
          if arr[i+1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[3])
      else:
        if arr[i,j]==0:
          mazeAvailableActions.setdefault((i,j),[])
        else:
          mazeAvailableActions.setdefault((i,j),[actions_dict[0],actions_dict[1],actions_dict[2],actions_dict[3]])
          if arr[i-1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[1]) 
          if arr[i+1,j]==0:
            mazeAvailableActions[i,j].remove(actions_dict[3])
          if arr[i,j+1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[2])
          if arr[i,j-1]==0:
            mazeAvailableActions[i,j].remove(actions_dict[0])

  return mazeAvailableActions

def makeMazeTransformationModel(mazeActs):
    mazeStateSpace={}
    for key in mazeActs:
      for action in mazeActs[key]:
        if action=='left':
          x=key[0]
          y=key[1]-1
          mazeStateSpace.setdefault(key,{})[action]=(x,y)
        elif action=='up':
          x=key[0]-1
          y=key[1]
          mazeStateSpace.setdefault(key,{})[action]=(x,y)
        elif action=='right':
          x=key[0]
          y=key[1]+1
          mazeStateSpace.setdefault(key,{})[action]=(x,y)
        elif action=='down':
          x=key[0]+1
          y=key[1]
          mazeStateSpace.setdefault(key,{})[action]=(x,y)
      if len(mazeActs[key])==0:
        mazeStateSpace.setdefault(key,{})

    return mazeStateSpace

def getFoodLocation(arr):
  x=np.where(arr == 2)[0][0]#1st food x
  y=np.where(arr == 2)[1][0]#1st food y
  return x,y

def getAllFoodLocations(arr):
    food_indices = np.where(arr == 2)
    return list(zip(food_indices[0], food_indices[1]))

def getGhostLocations(arr):
    ghost_indices = np.where(arr == 3)
    return list(zip(ghost_indices[0], ghost_indices[1]))

