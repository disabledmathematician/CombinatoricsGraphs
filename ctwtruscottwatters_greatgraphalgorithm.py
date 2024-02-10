#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Charles Truscott Watters
 
 I was searching for efficient code abstractions to describe graph theoretic algorithms 
 that are beneficial toward reducing visualisations, and in the same providing great
 tree call structures for dynamic programming or tree-diagram solution to computational
 problems. Including networkx and matplotlib visualisations in my neat little solution,
 but also is valid for the same computational solution structure described by the tree.
 Next a trinary tree and a kilominute interval between hypothetical indices structure
 of weights of randomly-generated stock prices, and a random walk through the tree
 (Can the true walk through a financial optimisation tree become a spanning tree out of all other hypothetical walks?)
 Charles Thomas Wallace Truscott Watters. 127 Broken Head Rd, Suffolk Park, NSW 2481
 
 UPDATE: Using itertools.permutations, which is likely Heap's algorithm or Steinhaus-Johnson-Trotter, for combinatorial orderings, and next colourings 
 of the vertices. Should be 5040. Can't wait to put this on Github.
 
"""
import networkx as nx
import matplotlib.pyplot as plt
import itertools
def Plot():
    n = 8
    count = 3
    while count == 3:
        L = [x for x in range(1, 2 ** count)]
        second_count = 1
        for n in itertools.permutations(L):
            plt.figure(second_count, dpi=95, figsize=[9, 9])
            i, j = 1, 2
            x = 0
            L2 = list(n)
            G = nx.Graph()
            while x < (len(L2) - ((len(L2) + 1) // 2)):
                G.add_edge(L2[x], L2[x + i])
                G.add_edge(L2[x], L2[x + j])
                i += 1
                j += 1
                x += 1
            plt.title("Charles Truscott Watters.".format(count))
            pos = nx.spring_layout(G, seed=5)
            nx.draw_networkx_nodes(G, pos, node_color='red', node_size=60)
            nx.draw_networkx_edges(G, pos, width=0.5)
            nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5, edge_color='grey', style='dashed')
            nx.draw_networkx_labels(G, pos, font_size=33, font_family='monospace')
            plt.savefig("CharlesTruscottWatters-CombinatorialOrdering-{}.png".format(second_count))
            second_count += 1
        count += 1

def CharlesTruscott():
    Plot()
    
CharlesTruscott()

