import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import lines


def drawGraph(gData, nodeColors,steps):
  G = nx.Graph(gData.g)
  #print(gData.g.keys())
  #print(nodeColors)
  #print(nodeColors.values())
  

  #node_color=[nodeColors[node] for node in gData.g.keys()]
  

  node_label_pos = {k:[v[0],v[1]-0.5]  for k,v in gData.locations.items()}
  edge_weights = {(k, v2) : k2 for k, v in gData.graph_dict.items() for k2, v2 in v.items()}#actions

  # set the size of the plot

  #plt.figure(figsize=(18, 13))
  

  # draw the graph (both nodes and edges) with locations
  nx.draw(G, pos={k: gData.locations[k] for k in G.nodes()},
            node_color=[nodeColors[node] for node in gData.g.keys()], 
            linewidths=0.3, edgecolors='k', node_size=100)
      
  # draw labels for nodes
  node_label_handles = nx.draw_networkx_labels(G, pos=node_label_pos, font_size=8)
  
  # add edge lables to the graph
  nx.draw_networkx_edge_labels(G, pos=gData.locations, edge_labels=edge_weights, font_size=8, font_color='r')
  # displaying the title
  plt.title('Search graph')
  # add a legend
  white_circle = lines.Line2D([], [], color="white", marker='o', markersize=10, markerfacecolor="white")
  orange_circle = lines.Line2D([], [], color="orange", marker='o', markersize=10, markerfacecolor="orange")
  red_circle = lines.Line2D([], [], color="red", marker='o', markersize=10, markerfacecolor="red")
  blue_circle = lines.Line2D([], [], color="blue", marker='o', markersize=10, markerfacecolor="blue")
  green_circle = lines.Line2D([], [], color="green", marker='o', markersize=10, markerfacecolor="green")
  plt.legend((white_circle, orange_circle, red_circle, blue_circle, green_circle),
               ('Un-explored', 'Frontier', 'Currently Exploring', 'Explored', 'Final Solution'),
               numpoints=1, prop={'size': 8}, loc=(1.25, .95))
  plt.show()
