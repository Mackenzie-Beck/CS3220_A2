#How do we decide which node from the frontier to expand next?
from nodeClass import Node
from queue import PriorityQueue
from collections import deque

def BestFirstSearchAgentProgram(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
    def program(problem):

      node = Node(problem.initial)
      #print(node)
      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))
      reached = {problem.initial:node}

      while frontier:
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))

        if problem.goal_test(node.state):
          print("We have found our goal: {}".format (node.state))
          return node

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                #print(child)
                print("The child node {}.".format(child))
                frontier.put((1,child))
                reached.update({child.state:child})
            
      return None

    return program

def BestFirstSearchAgentProgramForShow(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
  def program(problem):
      #print(111)
      steps = 0
      allNodeColors = []
      nodeColors = {k : 'white' for k in problem.graph.nodes()}

      node = Node(problem.initial)
      nodeColors[node.state] = "yellow"
      steps += 1
      allNodeColors.append(dict(nodeColors))

      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))

      nodeColors[node.state] = "orange"
      steps += 1
      allNodeColors.append(dict(nodeColors))



      reached = {problem.initial:node}

      while not frontier.empty():
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))
        nodeColors[node.state] = "red"
        steps += 1
        allNodeColors.append(dict(nodeColors))
        #print(node)

        if problem.goal_test(node.state):
          nodeColors[node.state] = "green"
          steps += 1
          allNodeColors.append(dict(nodeColors))
          return (node,steps,allNodeColors)
          

        #reached.add(node.state)
        #print(node.expand(problem))
        for child in node.expand(problem):
            #print(child)
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                print("The child node {}.".format(child))
                frontier.put((1,child))
                nodeColors[child.state] = "orange"
                steps += 1
                allNodeColors.append(dict(nodeColors))

                reached.update({child.state:child})

        # modify the color of explored nodes to blue
        nodeColors[node.state] = "blue"
        steps += 1
        allNodeColors.append(dict(nodeColors))
      print("No solution...")
            
      return None,steps,allNodeColors

  return program


def BreadthFirstSearchGraph():
  def program(problem):
    node = Node(problem.initial)
    #early goal test
    if problem.goal_test(node.state):
      print("We have found our goal: {}".format (node.state))
      return node
    
    frontier = deque()#FIFO
    frontier.append(node)
    reached = set()
    reached.add(node.state)
    
    while frontier:
      print("Reached: {} ".format(reached))
      print("Frontier: {} ".format(frontier))
      node = frontier.popleft()#FIFO
      print("The node {} is extracted from frontier:".format(node.state))
      
      for child in node.expand(problem):
        print("The child node {}.".format(child))
        if problem.goal_test(child.state):
          print("We have found our goal: {}".format (child.state))
          return child

        if child.state not in reached:
          reached.add(child.state)
          frontier.append(child)
    return None

  return program

def BreadthFirstSearchGraphForShow():
   def program(problem):
      steps = 0
      allNodeColors = []
      nodeColors = {k : 'white' for k in problem.graph.nodes()}

      node = Node(problem.initial)
      #early goal test
      if problem.goal_test(node.state):
        nodeColors[node.state] = "green"
        steps += 1
        allNodeColors.append(dict(nodeColors))
        return (node,steps,allNodeColors)
      
      frontier = deque()#FIFO
      frontier.append(node)

      nodeColors[node.state] = "orange"
      steps += 1
      allNodeColors.append(dict(nodeColors))

      reached = set()
      reached.add(node.state)

      while frontier:
         node = frontier.popleft()#FIFO
         print("The node {} is extracted from frontier:".format(node.state))
         nodeColors[node.state] = "red"
         steps += 1
         allNodeColors.append(dict(nodeColors))

         for child in node.expand(problem):
            print("The child node {}.".format(child))
            if problem.goal_test(child.state):
               print("We have found our goal: {}".format(child.state))
               nodeColors[child.state] = "green"
               steps += 1
               allNodeColors.append(dict(nodeColors))
               return (child,steps,allNodeColors)
            
            if child.state not in reached:
               reached.add(child.state)
               frontier.append(child)
         
         # modify the color of explored nodes to blue
         nodeColors[node.state] = "blue"
         steps += 1
         allNodeColors.append(dict(nodeColors))
      print("No solution...")

      return None,steps,allNodeColors
   
   return program

        
def DepthFirstSearchGraph():
  def program(problem):
    node = Node(problem.initial)
    #early goal test
    if problem.goal_test(node.state):
      print("We have found our goal: {}".format (node.state))
      return node
    
    frontier = deque()#LIFO
    frontier.append(node)
    reached = set()
    reached.add(node.state)
    
    while frontier:
      print("Reached: {} ".format(reached))
      print("Frontier: {} ".format(frontier))
      node = frontier.pop()#LIFO
      print("The node {} is extracted from frontier:".format(node.state))
      
      for child in node.expand(problem):
        print("The child node {}.".format(child))
        if problem.goal_test(child.state):
          print("We have found our goal: {}".format (child.state))
          return child

        if child.state not in reached:
          reached.add(child.state)
          frontier.append(child)
    return None

  return program



def LimitedDepthFirstSearchGraph(limit):
  def program(problem):
    node = Node(problem.initial)
    #early goal test
    if problem.goal_test(node.state):
      print("We have found our goal: {}".format (node.state))
      return node
    
    frontier = deque([(node, 0)]) # LIFO, with depth
    reached = set()
    reached.add(node.state)
    
    while frontier:
      print("Reached: {} ".format(reached))
      print("Frontier: {} ".format(frontier))
      node, depth = frontier.pop() # LIFO
      print("The node {} is extracted from frontier at depth {}:".format(node.state, depth))
      
      if depth < limit:
        for child in node.expand(problem):
          print("The child node {}.".format(child))
          if problem.goal_test(child.state):
            print("We have found our goal: {}".format (child.state))
            return child

          if child.state not in reached:
            reached.add(child.state)
            frontier.append((child, depth + 1))
    return None

  return program