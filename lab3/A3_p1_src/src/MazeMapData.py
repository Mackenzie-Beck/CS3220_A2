'''
mazeData = dict(
     A = dict(B = 7),
     C = dict(B = 6),
     F = dict(B = 2, E = 4, G = 4),
     D = dict(E = 2, M = 3),
     H = dict(G = 2, N = 3),
     I = dict(E = 2, J = 3, O = 2),
     L = dict(G = 2, K = 3, Q = 2),
     P = dict(O = 4, Q = 4, AD = 6),
     T = dict(O = 2, U = 2, Y = 2),
     W = dict(Q = 2, V = 2, Z = 2),
     X = dict(R = 3, Y = 2),
    AA = dict(S = 3, Z = 2),
    AC = dict(U = 4, AB = 4, AD = 2),
    AE = dict(V = 4, AD = 2, AF = 5)
)
'''

#Great for project. Not so much for this assignment.
'''
mazeData = dict(
     A = dict(B = 'East'),
     C = dict(B = 'West'),
     F = dict(B = 'South', E = 'West', G = 'East'),
     D = dict(E = 'East', M = 'North'),
     H = dict(G = 'West', N = 'North'),
     I = dict(E = 'South', J = 'East', O = 'North'),
     L = dict(G = 'South', K = 'West', Q = 'North'),
     P = dict(O = 'West', Q = 'East', AD = 'North'),
     T = dict(O = 'South', U = 'East', Y = 'North'),
     W = dict(Q = 'South', V = 'West', Z = 'North'),
     X = dict(R = 'South', Y = 'East'),
    AA = dict(S = 'South', Z = 'West'),
    AC = dict(U = 'South', AB = 'West', AD = 'East'),
    AE = dict(V = 'South', AD = 'West', AF = 'East')
)
'''


mazeData = dict(
     A = dict(B = 'Advance'),
     B = dict(A = 'Left', F = 'Advance', C = 'Right'),
     C = dict(B = 'Advance'),
     D = dict(M = 'Advance', E = 'Right'),
     E = dict(D = 'Left', I = 'Advance', F = 'Right'),
     F = dict(G = 'Left', B = 'Advance', E = 'Right'),
     G = dict(F = 'Left', L = 'Advance', H = 'Right'),
     H = dict(G = 'Left', N = 'Advance'),
     I = dict(O = 'Left', J = 'Advance', E = 'Right'),
     J = dict(I = 'Advance'),
     K = dict(L = 'Advance'),
     L = dict(G = 'Left', K = 'Advance', Q = 'Right'),
     M = dict(D = 'Advance'),
     N = dict(H = 'Advance'),
     O = dict(T = 'Left', P = 'Advance', I = 'Right'),
     P = dict(O = 'Left', AD = 'Advance', Q = 'Right'),
     Q = dict(L = 'Left', P = 'Advance', W = 'Right'),
     R = dict(X = 'Advance'),
     S = dict(AA = 'Advance'),
     T = dict(Y = 'Left', U = 'Advance', O = 'Right'),
     U = dict(T = 'Left', AC = 'Advance'),
     V = dict(AE = 'Advance', W = 'Right'),
     W = dict(Q = 'Left', V = 'Advance', Z = 'Right'),
     X = dict(Y = 'Left', R = 'Advance'),
     Y = dict(T = 'Left', X = 'Advance'),
     Z = dict(AA = 'Advance', W = 'Right'),
    AA = dict(S = 'Advance', Z = 'Right'),
    AB = dict(AC = 'Advance'),
    AC = dict(AD = 'Left', U = 'Advance', AB = 'Right'),
    AD = dict(AE = 'Left', P = 'Advance', AC = 'Right'),
    AE = dict(AF = 'Left', V = 'Advance', AD = 'Right'),
    AF = dict(AE = 'Advance')
)


'''
mazeData = dict(
     A = {'Advance' : 'B'},
     B = {'Left' : 'A', 'Advance' : 'F', 'Right' : 'C'},
     C = {'Advance' : 'B'},
     D = {'Advance' : 'M', 'Right' : 'E'},
     E = {'Left' : 'D', 'Advance' : 'I', 'Right' : 'F'},
     F = {'Left' : 'G', 'Advance' : 'B', 'Right' : 'E'},
     G = {'Left' : 'F', 'Advance' : 'L', 'Right' : 'H'},
     H = {'Left' : 'G', 'Advance' : 'N'},
     I = {'Left' : 'O', 'Advance' : 'J', 'Right' : 'E'},
     J = {'Advance' : 'I'},
     K = {'Advance' : 'L'},
     L = {'Left' : 'G', 'Advance' : 'K', 'Right' : 'Q'},
     M = {'Advance' : 'D'},
     N = {'Advance' : 'H'},
     O = {'Left' : 'T', 'Advance' : 'P', 'Right' : 'I'},
     P = {'Left' : 'O', 'Advance' : 'AD', 'Right' : 'Q'},
     Q = {'Left' : 'L', 'Advance' : 'P', 'Right' : 'W'},
     R = {'Advance' : 'X'},
     S = {'Advance' : 'AA'},
     T = {'Left' : 'Y', 'Advance' : 'U', 'Right' : 'O'},
     U = {'Left' : 'T', 'Advance' : 'AC'},
     V = {'Advance' : 'AE', 'Right' : 'W'},
     W = {'Left' : 'Q', 'Advance' : 'V', 'Right' : 'Z'},
     X = {'Left' : 'Y', 'Advance' : 'R'},
     Y = {'Left' : 'T', 'Advance' : 'X'},
     Z = {'Advance' : 'AA', 'Right' : 'W'},
    AA = {'Advance' : 'S', 'Right' : 'Z'},
    AB = {'Advance' : 'AC'},
    AC = {'Left' : 'AD', 'Advance' : 'U', 'Right' : 'AB'},
    AD = {'Left' : 'AE', 'Advance' : 'P', 'Right' : 'AC'},
    AE = {'Left' : 'AF', 'Advance' : 'V', 'Right' : 'AD'},
    AF = {'Advance' : 'AE'}
)
'''

mazeLocations = dict(
     A = (0,0),   B = (7,0),    C = (13,0),
     D = (1,2),   E = (3,2),    F = (7,2),
     G = (11,2),  H = (13,2),   I = (3,4),
     J = (6,4),   K = (8,4),    L = (11,4),
     M = (1,5),   N = (13,5),   O = (3,6),
     P = (7,6),   Q = (11,6),   R = (1,7),
     S = (13,7),  T = (3,8),    U = (5,8),
     V = (9,8),   W = (11,8),   X = (1,10),
     Y = (3,10),  Z = (11,10), AA = (13,10),
    AB = (1,12), AC = (5,12),  AD = (7,12),
    AE = (9,12), AF = (14,12),
)