import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = {'s': ['r', 'w'], 'r': ['v', 's'], 
         't': ['w', 'x', 'u'], 
         'u': ['t', 'x', 'y'], 
         'v': ['r'], 
         'w': ['s', 't', 'x'], 
         'x': ['w', 't', 'u', 'y'], 
         'y': ['x', 'u']}
    
    nodes, edges = get_nodes_edges(G)
    draw_graph(nodes, edges)

def get_nodes_edges(G):
  edges=[]
  nodes = []
  for node in G:
          nodes.append(node)
          for adjacent_node in G[node]:
              edges.append((adjacent_node,node))
  return(nodes, edges)

    
def draw_graph(nodes, edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(nodes)
    nx.draw_planar(G, with_labels=True)
    plt.show()

# Get the  tree edges
# Call this function only after dfs or bfs is called
def tree_edges(graph):
    tree_edges=[]
    for node in graph:
        if graph[node]['parent'] != None:
           tree_edges.append((node, graph[node]['parent']))
    return tree_edges



if __name__ == "__main__":
    main()