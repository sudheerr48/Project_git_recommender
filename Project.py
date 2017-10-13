#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:28:52 2017

@author: nagasudheerravela
"""

# Import necessary modules
import pickle
import networkx as nx
from nxviz import CircosPlot
import matplotlib.pyplot as plt
from itertools import combinations
from collections import defaultdict



#loaded pickle file into a variable G
G = pickle.load( open( "/Users/nagasudheerravela/Desktop/github_users.p", "rb" ) )





# Initialize the defaultdict: recommended
recommended = defaultdict(int)

# Iterate over all the nodes in G
for n, d in G.nodes(data=True):

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):
    
        # Check whether n1 and n2 do not have an edge
        if not G.has_edge(n1, n2):
        
            # Increment recommended
            recommended[(n1, n2)] += 1

# Identify the top 10 pairs of users
all_counts = sorted(recommended.values())
top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
print(top10_pairs)
