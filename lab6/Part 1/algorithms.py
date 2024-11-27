from queue import Queue

def AC3(csp):
  queue = Queue()
  
  print(f"Initial queue:")
  for Xi in csp.variables:
    for Xk in csp.neighbors[Xi]:
      queue.put((Xi, Xk))
      print((Xi, Xk), end=" ")
    print()
   
  csp.support_pruning()
  checks = 0
  while list(queue.queue):
    (Xi, Xj) = queue.get()
    #print(f'Arc {(Xi, Xj)} is cheking')
    revised, checks = revise(csp, Xi, Xj, checks)
    if revised:
      if not csp.curr_domains[Xi]:
        return False, checks  # CSP is inconsistent
      for Xk in csp.neighbors[Xi]:
        if Xk != Xj:
          queue.put((Xk, Xi))
    print(list(queue.queue))

    '''print(f'Arc {(Xj, Xi)} is cheking')
    revised, checks1 = back_revise(csp, Xi, Xj, checks)
    if revised:
      if not csp.curr_domains[Xj]:
        return False, checks  # CSP is inconsistent
      for Xk in csp.neighbors[Xj]:
        if Xk != Xi:
          queue.add((Xk, Xj))'''

      
  return True, checks  # CSP is satisfiable


def AC3v2(csp):
  queue = Queue()
  
  print(f"Initial queue:")
  for Xi in csp.variables:
    for Xk in csp.neighbors[Xi]:
      queue.put((Xi, Xk))
      print((Xi, Xk), end=" ")
    print()
   
  csp.support_pruning()
  checks = 0

  # Ensures that constraints have the backward direction to enforce arc-consistency.
  temp = csp.constraints
  for expression in temp:
    A,Ex,B = expression.split(' ')
    if Ex == '>':
      Ex = '<'
    elif Ex == '<':
      Ex = '>'
    else:
      continue
    newExpression = f'{B} {Ex} {A}'
    if newExpression not in csp.constraints:
      (csp.constraints).append(newExpression)

  while list(queue.queue):
    (Xi, Xj) = queue.get()
    #print(f'Arc {(Xi, Xj)} is cheking')

    # Takes the constraint that matches (Xi, Xj) from the list of constraints and creates a temporary lambda function implementing it.
    temp = csp.constraints
    for expression in temp:
      A,Ex,B = expression.split(' ')
      if A == Xi and B == Xj:
        csp.constraints = eval(f'lambda A, a, B, b: a {Ex} b')
        break  
    revised, checks = revise(csp, Xi, Xj, checks)
    csp.constraints = temp

    if revised:
      if not csp.curr_domains[Xi]:
        return False, checks  # CSP is inconsistent
      for Xk in csp.neighbors[Xi]:
        if Xk != Xj:
          queue.put((Xk, Xi))
    print(list(queue.queue))

    '''print(f'Arc {(Xj, Xi)} is cheking')
    revised, checks1 = back_revise(csp, Xi, Xj, checks)
    if revised:
      if not csp.curr_domains[Xj]:
        return False, checks  # CSP is inconsistent
      for Xk in csp.neighbors[Xj]:
        if Xk != Xi:
          queue.add((Xk, Xj))'''

      
  return True, checks  # CSP is satisfiable


def revise(csp, Xi, Xj, checks=0):
    """Return true if we remove a value."""
    revised = False
    print(f'Arc {(Xi, Xj)} is cheking')
    for x in csp.curr_domains[Xi][:]:
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        # if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
        conflict = True
        #print(csp.curr_domains[Xj])
        #print(csp.curr_domains[Xi])
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y):
                conflict = False
            checks += 1
            if not conflict:
                break
        if conflict:
            csp.prune(Xi, x)
            print(f'The val {x} was deleted from {Xi} domain')
            revised = True
    return revised, checks


def back_revise(csp, Xi, Xj, checks=0):
    """Return true if we remove a value."""
    revised = False
    for x in csp.curr_domains[Xi][:]:
        conflict = False
        for y in csp.curr_domains[Xj]:
            conflict = False
            #print(y)
            if csp.constraints(Xi, x, Xj, y)==False:
              #print(x,y)
              conflict = True
            checks +=1
            '''if not conflict:
                break'''
            if conflict:
              csp.prune(Xj, y)
              print(f'The val {y} was deleted from {Xj} domain')
              #print(y)
              revised = True
    return revised, checks