import networkx as nx
import matplotlib.pyplot as plt
from p3worlddata import p3world, create_room_dict

def simple_visualization(data=None):
    #create the graph using p3world dict
    G = nx.Graph(p3world)
    room_dict = create_room_dict()
    
    # set the size of the plot
    plt.figure(figsize=(10, 8))
    
    # draw the graph
    nx.draw(G, pos={room: coord for room, coord in room_dict.items()},
            node_color='pink', linewidths=0.3, edgecolors='k', node_size=3000)
    
    # displaying the title
    plt.title('Room Layout')
    
    # draw labels for nodes
    nx.draw_networkx_labels(G, pos={room: coord for room, coord in room_dict.items()}, font_size=10)
    
    plt.show()
