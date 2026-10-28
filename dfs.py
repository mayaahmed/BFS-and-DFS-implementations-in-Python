""" 
DFS algorithm
To run this program type
python dfs.py filename 
For Example:
python dfs.py bookeg.txt
"""

import get_adjacency_dict
import draw_graph
import sys

time = 0
def main():

     # get filename and source from command prompt
    if len(sys.argv) > 0:
        file = sys.argv[1]

    global time
    # read and initialize graph from file
    
    G = get_adjacency_dict.get_adjacency_list(file)
    graph = init_graph(G)

    
    # Call the dfs function on every node that is white
    for u in graph:
        if graph[u]['color'] == 'WHITE':
            dfs(graph, u)
    print(graph)

    # Draw the given graph
    nodes, edges = draw_graph.get_nodes_edges(G)
    draw_graph.draw_graph(nodes,edges)

     # Get edges of dfs forest and draw it
    dfs_tree_edges= draw_graph.tree_edges(graph)
    draw_graph.draw_graph(nodes,dfs_tree_edges)

#create a a graph as a dictionary of dictionaries with initialized distances and parents.
def init_graph(G):
  graph = {}
  for k in G:
    graph[k]={'node':k, 'adjacency_list': G[k], 'color':'WHITE', 'parent':None, 'd':0, 'f':0}
  return (graph)

# the DFS fnction
def dfs(graph, u):
    global time
    time = time+1
    graph[u]['d']=time
    graph[u]['color']='GRAY'
   
    for  v in graph[u]['adjacency_list']:
        if graph[v]['color'] == 'WHITE':
            graph[v]['parent'] = u
            dfs(graph, v)
    graph[u]['color']='BLACK'
    time = time+1
    graph[u]['f']=time
    
    

    





   




if __name__ == "__main__":
    main()
