# BFS algorithm
""" To run this program type
python bfs.py filename source
For Example:
python bfs.py graphsource_s.txt 's' 

"""

import math
import draw_graph
import get_adjacency_dict
import sys



def main(): 

     # get filename and source from command prompt
    if len(sys.argv) > 1:
        file = sys.argv[1]
        source = sys.argv[2]
    
    # Read and initialize distances, color,  and parents. Also get the adjacency list.  
   
    G = get_adjacency_dict.get_adjacency_list(file)
    graph= init_graph(G)
    
    # run bfs on graph
    graph = bfs(graph, graph[source])

    for v in graph:
        print(f"A shortest path from  {v} to  {source}:")
        print_path(graph, source, v)
        print("")

    # Draw the given graph
    nodes, edges = draw_graph.get_nodes_edges(G)
    draw_graph.draw_graph(nodes,edges)
        
    # Draw the  bfs tree
    tree_edges= draw_graph.tree_edges(graph)
    draw_graph.draw_graph(nodes,tree_edges)

#create a a graph as a dictionary of dictionaries with initialized distances, colors, and parents.
def init_graph(G):
  graph = {}
  for k in G:
    graph[k]={'node':k, 'adjacency_list': G[k], 'distance':math.inf, 'parent':None, 'color': 'White'}
  return (graph)

# The BFS function
def bfs(graph, source):
    #initial steps 
    queue = []     #Initialize a queue
    source['distance']=0
    queue.append(source)     #Initialize a queue. queue contains nodes with their associated dictionaries

    #First in first out queue
    while queue:
        u = queue.pop(0) 
        u['color'] = 'Black'
        # Look at  all the nodes adjacent to u
        for  v in u['adjacency_list']:
                if graph[v]['color'] == 'White':
                    graph[v]['distance'] = u['distance']+1
                    graph[v]['color'] = 'Gray'
                    if(u['node']):
                        graph[v]['parent'] = u['node']
                    queue.append(graph[v])
    return graph


# run a recursive function on parents of a node till we reach the source.
def print_path(graph, source, v):
    if v == source:
        print(source,  end="")
    elif graph[v]['parent'] == None:  # v is not reachable from the source
        print(f"no path from {source} to {v} exists" )
    else:
        print_path(graph, source, graph[v]['parent'])
        print(v, end="")


if __name__ == "__main__":
    main()
