


r1a, r1b, r1c, r2a, r2b, r2c = 'Room1_A', 'Room1_B', 'Room1_C', 'Room2_A', 'Room2_B', 'Room2_C'


p3world={
    r1a: {r1b: 1, r2a: 1},
    r1b: {r1a: 1, r1c: 1},
    r1c: {r1b: 1, r2c: 1},
    r2a: {r1a: 1, r2b: 1},
    r2b: {r2a: 1, r2c: 1},
    r2c: {r1c: 1, r2b: 1}
}




