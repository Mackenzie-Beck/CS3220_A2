from locations_cfh import *

# lookup table for the cat friendly house
# Did not enjoy this

feedingRules = {
    #start in room 1


    #Empty room 1
    (room1, 'Empty'): 'moveright',


    #Empty room 1, Sausage room 2
    ((room1, 'Empty'), (room2, 'SausageHere')): 'eat',
    ((room1, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty')): 'moveright',
    ((room1, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty'), (room3, 'MilkHere')): 'drink',
    ((room1, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty'), (room3, 'MilkHere'), (room3, 'Empty')): 'stop',


    


    #Empty room 1, Milk room 2
    ((room1, 'Empty'), (room2, 'MilkHere')): 'drink',
    ((room1, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty')): 'moveright',
    ((room1, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty'), (room3, 'SausageHere')): 'eat',
    ((room1, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty'), (room3, 'SausageHere'), (room3, 'Empty')): 'stop',
    



    #Sausage room 1
    (room1, 'SausageHere'): 'eat',
    ((room1, 'SausageHere'), (room1, 'Empty')): 'moveright',

    #Sausage room1 milk room 3
    ((room1, 'SausageHere'), (room1, 'Empty'), (room2, 'Empty')): 'moveright',
    ((room1, 'SausageHere'), (room1, 'Empty'), (room2, 'Empty'), (room3, 'MilkHere')): 'drink',
    ((room1, 'SausageHere'), (room1, 'Empty'), (room2, 'Empty'), (room3, 'MilkHere'), (room3, 'Empty')): 'stop',

    # Sausage room 1, Milk room 2
    ((room1, 'SausageHere'), (room1, 'Empty'), (room2, 'MilkHere')): 'drink',
    ((room1, 'SausageHere'), (room1, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty')): 'moveright',
    ((room1, 'SausageHere'), (room1, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty'), (room3, 'Empty')): 'stop',




    # Milk room 1
    (room1, 'MilkHere'): 'drink',
    ((room1, 'MilkHere'), (room1, 'Empty')): 'moveright',

    # Milk room 1 Sausage room 3
    ((room1, 'MilkHere'), (room1, 'Empty'), (room2, 'Empty')): 'moveright',
    ((room1, 'MilkHere'), (room1, 'Empty'), (room2, 'Empty'), (room3, 'SausageHere')): 'eat',
    ((room1, 'MilkHere'), (room1, 'Empty'), (room2, 'Empty'), (room3, 'SausageHere'), (room3, 'Empty')): 'stop',

    # Milk room 1, Sausage room 2
    ((room1, 'MilkHere'), (room1, 'Empty'), (room2, 'SausageHere')): 'eat',
    ((room1, 'MilkHere'), (room1, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty')): 'moveright',
    ((room1, 'MilkHere'), (room1, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty'), (room3, 'Empty')): 'stop',




    #Start in room 3

    #Empty room 3
    (room3, 'Empty'): 'moveleft',


    #Empty room 3, Sausage room 2
    ((room3, 'Empty'), (room2, 'SausageHere')): 'eat',
    ((room3, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty')): 'moveleft',
    ((room3, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty'), (room1, 'MilkHere')): 'drink',
    ((room3, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty'), (room1, 'MilkHere'), (room1, 'Empty')): 'stop',



    #Empty room 3, Milk room 2
    ((room3, 'Empty'), (room2, 'MilkHere')): 'drink',
    ((room3, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty')): 'moveleft',
    ((room3, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty'), (room1, 'SausageHere')): 'eat',
    ((room3, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty'), (room1, 'SausageHere'), (room1, 'Empty')): 'stop',


    # Sausage room 3
    (room3, 'SausageHere'): 'eat',
    ((room3, 'SausageHere'), (room3, 'Empty')): 'moveleft',


    # Sausage room 3, Milk room 2
    ((room3, 'SausageHere'), (room3, 'Empty'), (room2, 'MilkHere')): 'drink',
    ((room3, 'SausageHere'), (room3, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty')): 'moveleft',
    ((room3, 'SausageHere'), (room3, 'Empty'), (room2, 'MilkHere'), (room2, 'Empty'), (room1, 'Empty')): 'stop',


    # Sausage room 3, Milk room 1
    ((room3, 'SausageHere'), (room3, 'Empty'), (room2, 'Empty')): 'moveleft',
    ((room3, 'SausageHere'), (room3, 'Empty'), (room2, 'Empty'), (room1, 'MilkHere')): 'drink',
    ((room3, 'SausageHere'), (room3, 'Empty'), (room2, 'Empty'), (room1, 'MilkHere'), (room1, 'Empty')): 'stop',
    
    
    #Milk room 3
    (room3, 'MilkHere'): 'drink',
    ((room3, 'MilkHere'), (room3, 'Empty')): 'moveleft',


    #Milk room 3, Sausage room 2
    ((room3, 'MilkHere'), (room3, 'Empty'), (room2, 'SausageHere')): 'eat',
    ((room3, 'MilkHere'), (room3, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty')): 'moveleft',
    ((room3, 'MilkHere'), (room3, 'Empty'), (room2, 'SausageHere'), (room2, 'Empty'), (room1, 'Empty')): 'stop',


    #Milk room 3, Sausage room 1
    ((room3, 'MilkHere'), (room3, 'Empty'), (room2, 'Empty')): 'moveleft',
    ((room3, 'MilkHere'), (room3, 'Empty'), (room2, 'Empty'), (room1, 'SausageHere')): 'eat',
    ((room3, 'MilkHere'), (room3, 'Empty'), (room2, 'Empty'), (room1, 'SausageHere'), (room1, 'Empty')): 'stop',




    #Start in room 2

    #Empty room 2
    (room2, 'Empty'): 'moveright',


    #Empty room 2, Sausage room 1, milk room 3
    ((room2, 'Empty'), (room3, 'MilkHere')): 'drink',
    ((room2, 'Empty'), (room3, 'MilkHere'), (room3, 'Empty')): 'moveleft',
    ((room2, 'Empty'), (room3, 'MilkHere'), (room3, 'Empty'), (room2, 'Empty')): 'moveleft',
    ((room2, 'Empty'), (room3, 'MilkHere'), (room3, 'Empty'), (room2, 'Empty'), (room1, 'SausageHere')): 'eat',
    ((room2, 'Empty'), (room3, 'MilkHere'), (room3, 'Empty'), (room2, 'Empty'), (room1, 'SausageHere'), (room1, 'Empty')): 'stop',

    

    #Sausage room2, Milk room 3, empty room 1
    (room2, 'SausageHere'): 'eat',
    ((room2, 'SausageHere'), (room2, 'Empty')): 'moveright',
     ((room2, 'SausageHere'), (room2, 'Empty'), (room3, 'MilkHere')): 'drink',
     ((room2, 'SausageHere'), (room2, 'Empty'), (room3, 'MilkHere'), (room3, 'Empty')): 'stop',


     #Milk room 2, Sausage room 3, empty room 1
    (room2, 'MilkHere'): 'drink',
    ((room2, 'MilkHere'), (room2, 'Empty')): 'moveright',
    ((room2, 'MilkHere'), (room2, 'Empty'), (room3, 'SausageHere')): 'eat',
    ((room2, 'MilkHere'), (room2, 'Empty'), (room3, 'SausageHere'), (room3, 'Empty')): 'stop',

}
