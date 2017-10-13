#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:10:19 2017
Thanks to Eric Ma for tutorial on nxviz
@author: nagasudheerravela
"""
import pickle
import networkx as nx
import matplotlib.pyplot as plt
from nxviz.plots import ArcPlot
from nxviz import MatrixPlot
from itertools import combinations



#loaded pickle file into a variable G
G = pickle.load( open( "/Users/nagasudheerravela/Desktop/github_users.p", "rb" ) )

#printing the type of variable G
print(type(G))

#plotting the network
nx.draw(G)
plt.show()


#printing nodes in graph
print(G.nodes())

#printing number of total nodes in graph
print(len(list(G.nodes())))

#printing edges in graph
print(len(list(G.edges())))

#printing first 10 nodes data with metadata
nodes_1_10 = [n for n,d in G.nodes(data=True) ]

#Plotting Graph using matrix plot

# Create the MatrixPlot object: m
m = nv.MatrixPlot(G)

# Draw m to the screen
m.draw()

# Display the plot
plt.show()

#To check whether my graph has any self nodes 
# Define find_selfloop_nodes()
def find_number_selfloop_nodes(G):
    """
    Finds all nodes that have self-loops in the graph G.
    """
    nodes_in_selfloops = []
    
    # Iterate over all the edges of G
    for u, v in G.edges():
    
    # Check if node u and node v are the same
        if u == v:
        
            # Append node u to nodes_in_selfloops
            nodes_in_selfloops.append(u)
            
    return nodes_in_selfloops

# Check whether number of self loops equals the number of nodes in self loops
print(len(find_number_selfloop_nodes(G)))
print(G.number_of_selfloops() )

#To findout each neighbour nodes
# Define nodes_with_m_nbrs()
def nodes_with_m_nbrs(G,m):
    """
    Returns all nodes in graph G that have m neighbors.
    """
    nodes = set()
    
    # Iterate over all nodes in G
    for n in G.nodes():
    
        # Check if the number of neighbors of n matches m
        if len(G.neighbors(n)) == m:
        
            # Add the node n to the set
            nodes.add(n)
            
    # Return the nodes with m neighbors
    return nodes

#For finding nodes having only one neighbour
OneNeighbour_nodes = nodes_with_m_nbrs(G,1)
print(OneNeighbour_nodes)
    

def List_nodes_with_max_nbrs(G):
    """
    Returns all nodes in graph G that have maximum count of neighbors.
    """
    nodes_by_neighborcount = [None]*len(list(G.nodes()))
    
    # Iterating over all nodes in G
    for n in range(len(list(G.nodes()))):
          
        # checking node neighbour count i am starting from 1 than 0 
        if ( n != 0 ):
            
            #Adding nodes having same number of neighbors in one list and adding all those lists together  
           nodes_by_neighborcount[n] = nodes_with_m_nbrs(G,n)
            
             
           max_nmbr = len(nodes_by_neighborcount[n])
    return  nodes_by_neighborcount
# try to use this function only if u have a good RAM  because it is taking a lot of time 
List_check = List_nodes_with_max_nbrs(G)
 
    
    
#If you think the above task takes lot of time and processing ,you can go through neighbors method 
#and we will calculate degree    
#Computing  degree distribution
  
# Compute the degree of every node: degrees
degrees = [len(G.neighbors(n)) for n in G.nodes()]

# Print the degrees
print(degrees)
 
#maximum degree calculation

Max_degree = max(degrees) 
print(Max_degree)

#nodes having maximum degee
m = []
Max_node = [i for i in G.nodes() if len(G.neighbors(i)) == Max_degree]

print(Max_node)

# Compute the degree centrality of the Github network: deg_cent
deg_cent = nx.degree_centrality(G)

# Plot a histogram of the degree centrality distribution of the graph
plt.figure()
plt.ylabel('Degree centre values')
plt.xlabel('nodes')
plt.hist(list(deg_cent.values()))
plt.show()

# Plot a histogram of the degree distribution of the graph
plt.figure()
plt.ylabel('Degree values')
plt.xlabel('nodes')
plt.hist(degrees)
plt.show()

# Plot a scatter plot of the centrality distribution and the degree distribution
plt.figure()
plt.xlabel('degrees')
plt.ylabel('Degree centre values')
plt.scatter(degrees, list(deg_cent.values()))
plt.show()

#obseravation:- we can clearly observe positive correlation between degrees and degree centrality of network

# Compute the betweenness centrality of G: bet_cen
bet_cen = nx.betweenness_centrality(G)
# Create a scatter plot of betweenness centrality and degree centrality
plt.scatter(list(bet_cen.values()) ,list(deg_cent.values()))
# Display the plot
plt.show()




# Calculate the largest connected component subgraph: largest_ccs
largest_ccs = sorted(nx.connected_component_subgraphs(G), key=lambda x: len(x))[-1]

# Create the customized MatrixPlot object: h
h = MatrixPlot(graph = largest_ccs )

# Draw the MatrixPlot to the screen
h.draw()
plt.show()

# Iterate over all the nodes in G, including the metadata
for n, d in G.nodes(data=True):

    # Calculate the degree of each node: G.node[n]['degree']
    G.node[n]['degree'] = nx.degree(G,n)
    
# Create the ArcPlot object: a
a = ArcPlot(graph = G ,node_order = 'degree')

# Draw the ArcPlot to the screen
a.draw()
plt.show()














    
