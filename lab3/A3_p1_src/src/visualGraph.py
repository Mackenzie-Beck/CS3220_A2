import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import lines


def drawGraph(gData, nodeColors, nodeStatuses):
  G = nx.DiGraph()

  # Add nodes with their statuses
  for node in gData.graph:
    G.add_node(node, status=nodeStatuses.get(node))

  # Add edges with actions as labels
  for node, edges in gData.graph.items():
    print(edges)
    for neighbor, action in edges.items():
      G.add_edge(node, neighbor, action=action)


  # Set node colors based on their status
  color_map = {
      'unexplored': 'white',
      'expanded': 'red',
      'onTheFrontier': 'orange',
      'goal': 'green'
  }
  node_color_list = [color_map[G.nodes[node].get('status', 'unexplored')] for node in G.nodes()]

  # Draw the graph
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True, node_color=node_color_list, edgecolors='k', node_size=400, font_size=10, font_weight='bold')

  # Draw edge labels
  edge_labels = {(u, v): d['action'] for u, v, d in G.edges(data=True)}
  nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

  # Create a legend for the node colors
  legend_elements = [
      lines.Line2D([0], [0], marker='o', color='w', markerfacecolor='white', markersize=10, label='Unexplored'),
      lines.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Expanded'),
      lines.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='On the Frontier'),
      lines.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Goal')
  ]
  plt.legend(handles=legend_elements, loc='best')

  plt.show()
