#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 03:58:09 2024

@author: thinkpad
"""
import networkx as nx
import matplotlib.pyplot as plt

plt.figure(0, dpi=600, figsize=[10, 10])
plt.title("I love you Dad Mark William Watters. Thank you Harvard University and MIT")
g = nx.Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("B", "E")
g.add_edge("C", "F")
g.add_edge("C", "G")
g.add_edge("D", "H")
g.add_edge("D", "I")
g.add_edge("E", "J")
g.add_edge("E", "K")
g.add_edge("F", "L")
g.add_edge("F", "M")
g.add_edge("G", "N")
g.add_edge("G", "O")

nx.draw(g, with_labels = True)
plt.savefig('g.png')