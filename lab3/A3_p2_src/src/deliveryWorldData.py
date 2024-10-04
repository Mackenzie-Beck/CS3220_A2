import random

s,a,b,g='room1','room2','room3','room4'

deliveryWorld={
s:{a:1, b:1},
a:{b:1, g:1},
b:{a:1, g:1},
g:{a:1, b:1}
}

def roomLocations():
  x = []
  y = []
  n=len(deliveryWorld.keys())
  for _ in range(n):
    x.append(random.randint(0, n+1))
    y.append(random.randint(0, n+1))
  zipped = zip(x, y)
  return dict(zip(deliveryWorld.keys(), zipped))