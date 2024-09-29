from locations_cfh import *

# lookup table for the cat friendly house
# Did not enjoy this

feedingRules = {
    #start in room 1


    #Empty room 1
    ((1, 'Empty'),): 'moveright',


    #Empty room 1, Sausage room 2
    ((1, 'Empty'), (2, 'SausageHere')): 'eat',
    ((1, 'Empty'), (2, 'SausageHere'), (2, 'Empty')): 'moveright',
    ((1, 'Empty'), (2, 'SausageHere'), (2, 'Empty'), (3, 'MilkHere')): 'drink',
    ((1, 'Empty'), (2, 'SausageHere'), (2, 'Empty'), (3, 'MilkHere'), (3, 'Empty')): 'stop',


    


    #Empty room 1, Milk room 2
    ((1, 'Empty'), (2, 'MilkHere')): 'drink',
    ((1, 'Empty'), (2, 'MilkHere'), (2, 'Empty')): 'moveright',
    ((1, 'Empty'), (2, 'MilkHere'), (2, 'Empty'), (3, 'SausageHere')): 'eat',
    ((1, 'Empty'), (2, 'MilkHere'), (2, 'Empty'), (3, 'SausageHere'), (3, 'Empty')): 'stop',
    



    #Sausage room 1
    ((1, 'SausageHere'),): 'eat',
    ((1, 'SausageHere'), (1, 'Empty')): 'moveright',

    #Sausage room1 milk room 3
    ((1, 'SausageHere'), (1, 'Empty'), (2, 'Empty')): 'moveright',
    ((1, 'SausageHere'), (1, 'Empty'), (2, 'Empty'), (3, 'MilkHere')): 'drink',
    ((1, 'SausageHere'), (1, 'Empty'), (2, 'Empty'), (3, 'MilkHere'), (3, 'Empty')): 'stop',

    # Sausage room 1, Milk room 2
    ((1, 'SausageHere'), (1, 'Empty'), (2, 'MilkHere')): 'drink',
    ((1, 'SausageHere'), (1, 'Empty'), (2, 'MilkHere'), (2, 'Empty')): 'moveright',
    ((1, 'SausageHere'), (1, 'Empty'), (2, 'MilkHere'), (2, 'Empty'), (3, 'Empty')): 'stop',




    # Milk room 1
    ((1, 'MilkHere'),): 'drink',
    ((1, 'MilkHere'), (1, 'Empty')): 'moveright',

    # Milk room 1 Sausage room 3
    ((1, 'MilkHere'), (1, 'Empty'), (2, 'Empty')): 'moveright',
    ((1, 'MilkHere'), (1, 'Empty'), (2, 'Empty'), (3, 'SausageHere')): 'eat',
    ((1, 'MilkHere'), (1, 'Empty'), (2, 'Empty'), (3, 'SausageHere'), (3, 'Empty')): 'stop',

    # Milk room 1, Sausage room 2
    ((1, 'MilkHere'), (1, 'Empty'), (2, 'SausageHere')): 'eat',
    ((1, 'MilkHere'), (1, 'Empty'), (2, 'SausageHere'), (2, 'Empty')): 'moveright',
    ((1, 'MilkHere'), (1, 'Empty'), (2, 'SausageHere'), (2, 'Empty'), (3, 'Empty')): 'stop',




    #Start in room 3

    #Empty room 3
    ((3, 'Empty'),): 'moveleft',


    #Empty room 3, Sausage room 2
    ((3, 'Empty'), (2, 'SausageHere')): 'eat',
    ((3, 'Empty'), (2, 'SausageHere'), (2, 'Empty')): 'moveleft',
    ((3, 'Empty'), (2, 'SausageHere'), (2, 'Empty'), (1, 'MilkHere')): 'drink',
    ((3, 'Empty'), (2, 'SausageHere'), (2, 'Empty'), (1, 'MilkHere'), (1, 'Empty')): 'stop',



    #Empty room 3, Milk room 2
    ((3, 'Empty'), (2, 'MilkHere')): 'drink',
    ((3, 'Empty'), (2, 'MilkHere'), (2, 'Empty')): 'moveleft',
    ((3, 'Empty'), (2, 'MilkHere'), (2, 'Empty'), (1, 'SausageHere')): 'eat',
    ((3, 'Empty'), (2, 'MilkHere'), (2, 'Empty'), (1, 'SausageHere'), (1, 'Empty')): 'stop',


    # Sausage room 3
    ((3, 'SausageHere'),): 'eat',
    ((3, 'SausageHere'), (3, 'Empty')): 'moveleft',


    # Sausage room 3, Milk room 2
    ((3, 'SausageHere'), (3, 'Empty'), (2, 'MilkHere')): 'drink',
    ((3, 'SausageHere'), (3, 'Empty'), (2, 'MilkHere'), (2, 'Empty')): 'moveleft',
    ((3, 'SausageHere'), (3, 'Empty'), (2, 'MilkHere'), (2, 'Empty'), (1, 'Empty')): 'stop',


    # Sausage room 3, Milk room 1
    ((3, 'SausageHere'), (3, 'Empty'), (2, 'Empty')): 'moveleft',
    ((3, 'SausageHere'), (3, 'Empty'), (2, 'Empty'), (1, 'MilkHere')): 'drink',
    ((3, 'SausageHere'), (3, 'Empty'), (2, 'Empty'), (1, 'MilkHere'), (1, 'Empty')): 'stop',
    
    
    #Milk room 3
    ((3, 'MilkHere'),): 'drink',
    ((3, 'MilkHere'), (3, 'Empty')): 'moveleft',


    #Milk room 3, Sausage room 2
    ((3, 'MilkHere'), (3, 'Empty'), (2, 'SausageHere')): 'eat',
    ((3, 'MilkHere'), (3, 'Empty'), (2, 'SausageHere'), (2, 'Empty')): 'moveleft',
    ((3, 'MilkHere'), (3, 'Empty'), (2, 'SausageHere'), (2, 'Empty'), (1, 'Empty')): 'stop',


    #Milk room 3, Sausage room 1
    ((3, 'MilkHere'), (3, 'Empty'), (2, 'Empty')): 'moveleft',
    ((3, 'MilkHere'), (3, 'Empty'), (2, 'Empty'), (1, 'SausageHere')): 'eat',
    ((3, 'MilkHere'), (3, 'Empty'), (2, 'Empty'), (1, 'SausageHere'), (1, 'Empty')): 'stop',




    #Start in room 2

    #Empty room 2
    ((2, 'Empty'),): 'moveright',


    #Empty room 2, Sausage room 1, milk room 3
    ((2, 'Empty'), (3, 'MilkHere')): 'drink',
    ((2, 'Empty'), (3, 'MilkHere'), (3, 'Empty')): 'moveleft',
    ((2, 'Empty'), (3, 'MilkHere'), (3, 'Empty'), (2, 'Empty')): 'moveleft',
    ((2, 'Empty'), (3, 'MilkHere'), (3, 'Empty'), (2, 'Empty'), (1, 'SausageHere')): 'eat',
    ((2, 'Empty'), (3, 'MilkHere'), (3, 'Empty'), (2, 'Empty'), (1, 'SausageHere'), (1, 'Empty')): 'stop',

    

    #Sausage room2, Milk room 3, empty room 1
    ((2, 'SausageHere'),): 'eat',
    ((2, 'SausageHere'), (2, 'Empty')): 'moveright',
     ((2, 'SausageHere'), (2, 'Empty'), (3, 'MilkHere')): 'drink',
     ((2, 'SausageHere'), (2, 'Empty'), (3, 'MilkHere'), (3, 'Empty')): 'stop',


     #Milk room 2, Sausage room 3, empty room 1
    ((2, 'MilkHere'),): 'drink',
    ((2, 'MilkHere'), (2, 'Empty')): 'moveright',
    ((2, 'MilkHere'), (2, 'Empty'), (3, 'SausageHere')): 'eat',
    ((2, 'MilkHere'), (2, 'Empty'), (3, 'SausageHere'), (3, 'Empty')): 'stop',

}
