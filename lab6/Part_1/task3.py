var1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
var2 = range(1,10)

vars = set()

for letter in var1:
    for number in var2:
        vars.add((letter + str(number)))

sudokuNeighbors={}


#add cells in asterisk pattern to make asterisk sudoku

for letter in var1:
    for number in var2:
        cell = letter + str(number)
        neighbors = set()


        asterisk_neighbors = set()
        asterisk_neighbors.add('B5')
        asterisk_neighbors.add('C3')
        asterisk_neighbors.add('C7')
        asterisk_neighbors.add('E2')
        asterisk_neighbors.add('E5')
        asterisk_neighbors.add('E8')
        asterisk_neighbors.add('G3')
        asterisk_neighbors.add('G7')
        asterisk_neighbors.add('H5')

        
        # Add all cells in the same row
        for l in var1:
            if l != letter:
                neighbors.add(l + str(number))
        
        # Add all cells in the same column
        for n in var2:
            if n != number:
                neighbors.add(letter + str(n))
        
        # Add all cells in the same 3x3 box
        box_row = (ord(letter) - ord('A')) // 3
        box_col = (number - 1) // 3
        for l in var1[box_row*3:(box_row+1)*3]:
            for n in range(box_col*3 + 1, box_col*3 + 4):
                if l + str(n) != cell:
                    neighbors.add(l + str(n))
        
        if cell in asterisk_neighbors:
            asterisk_neighbors.remove(cell)
            neighbors.update(asterisk_neighbors)

        sudokuNeighbors[cell] = list(neighbors)



sudoku_start_config = {
    'A2': '1', 'A8': '6', 'B1': '3', 'B3': '9', 'B7': '1', 'B9': '5',
    'C2': '8', 'C4': '3', 'C6': '5', 'C8': '7', 
    'D3': '2', 'D5': '7', 'D7': '8',
    'E4': '6', 'E6': '8',
    'F3': '8', 'F5': '9', 'F7': '2',
    'G2': '2', 'G4': '4', 'G6': '1', 'G8': '9',
    'H1': '9', 'H3': '4', 'H7': '6', 'H9': '1',
    'I2': '3', 'I8': '8'
        }


sudokuDomains={var:[sudoku_start_config[var]] if var in sudoku_start_config else [str(ch) for ch in range(1,10)] for var in sudokuNeighbors.keys()}
sudokuDomains

def sudokuConstraints1(X, x, Y, y):
    """
    Returns True if the assignment of x to X and y to Y satisfies the constraint.
    For Sudoku: values must be different if they're neighbors
    """
    # If either cell has no value, there's no constraint violation
    if not x or not y:
        return True
    # Otherwise, values must be different
    return x != y


from CSPclass import CSPBasic
basicSuokuCSP=CSPBasic(variables=sudokuNeighbors.keys(), neighbors=sudokuNeighbors,domains=sudokuDomains, constraints=sudokuConstraints1)

from algorithms import AC3
from algorithms import AC3v2

AC3(basicSuokuCSP)

for var in basicSuokuCSP.variables:
    print(var, basicSuokuCSP.curr_domains[var])

