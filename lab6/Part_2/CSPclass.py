from problemClass import Problem
from utils import count

class CSPBasic(Problem):
      def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem. If variables is empty, it becomes domains.keys()."""
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0

      # These are for constraint propagation

      def support_pruning(self):
        """Make sure we can prune values from domains. 
        (We want to pay for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

      def prune(self, var, value):
        """Rule out var=value."""
        if value in self.curr_domains[var]:
            self.curr_domains[var].remove(value)


      def remove_from_domains(self,value):
        for var in self.variables:
            self.prune(var,value)


class CSP(CSPBasic):
  def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val
        self.nassigns += 1

  def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            del assignment[var]

  def nconflicts(self, var, val, assignment):
        """Return the number of conflicts var=val has with other variables."""
        # Count conflicts with neighbors
        def conflict(var2):
            return (var2 in assignment and
                    not self.constraints(var, val, var2, assignment[var2]))
        
        conflicts = count(conflict(v) for v in self.neighbors[var])
       # print(f'Checking conflicts for {var}={val}: {conflicts} conflicts')
        return conflicts

  def display(self, assignment):
        """Show a human-readable representation of the CSP."""
        print(assignment)

  def choices(self, var):
        """Return all values for var that aren't currently ruled out."""
        return (self.curr_domains or self.domains)[var]

class DinnerCSP(CSP):
    def __init__(self, variables, domains, neighbors, constraints):
        super().__init__(variables, domains, neighbors, constraints)

    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        super().assign(var, val, assignment)
        self.variables.remove(var)

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment and add the variable back to the list of variables."""
        super().unassign(var, assignment)
        self.variables.append(var)
