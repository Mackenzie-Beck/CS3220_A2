import networkx as nx
import matplotlib.pyplot as plt

def simple_visualization(data):
  G = nx.Graph(data.graph_dict)
  #print(data.locations.items())
  nodes_colors= ['pink' for node in data.graph_dict.keys()]
  # set the size of the plot
  plt.figure(figsize=(20, 15))
  #draw the graph (both nodes and edges) with locations from romania_locations
  nx.draw(G, pos={k: data.locations[k] for k in G.nodes()},
            node_color=nodes_colors, linewidths=0.3, edgecolors='k')
  # displaying the title
  plt.title('Delivery graph')
  node_label_pos = { k:[v[0],v[1]]  for k,v in data.locations.items() }
  print(node_label_pos)
  # draw labels for nodes
  nx.draw_networkx_labels(G, pos=node_label_pos, font_size=15)
  #nx.draw_networkx_labels(G,node_label_pos, G.nodes, font_color='r')
  plt.show()
