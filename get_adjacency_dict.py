# This program reads a graph from a file and initializes it.
import math

def main():
    file = 'bookeg.txt'
    G = get_adjacency_list(file)
    print(G)



def get_adjacency_list(file):

    # Get a dictionary of the adjacency list from the file
    G = {}
    with open(file, 'r') as file:
        #For each line in the file separate the node and the list of adjacent nodes
        for line in file:
            node, list = line.split(':')
            node = node.strip()
            list = list.strip()
            if(list):
                adj = list.split(',') #create an array of adjacent list
            else:
                adj = []

            G[node] = adj  # Assign adjacent list to node
    return(G)

   




if __name__ == "__main__":
    main()