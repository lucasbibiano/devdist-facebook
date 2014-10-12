# -*- coding: utf-8 -*-
import networkx as nx
from os import system
import random

def print_info(G):
  #info prints name, type, number of nodes and edges, and average degree already
  print(nx.info(G))
  print "Density: ", nx.density(G)
  print "Number of connected components: ", nx.number_connected_components(G)

  all_degree_cent = nx.degree_centrality(G)
  all_bet_cent = nx.betweenness_centrality(G)
  all_close_cent = nx.closeness_centrality(G)
  
  oldest = []
  agerank = 0
  
  names = []
  
  print ("Node, Degree Centrality, Betweenness Centrality, Closeness Centrality:")
  for x in range(G.number_of_nodes()):
    names.append(G.nodes(data=True)[x][1]['label'])
    
    if G.nodes(data=True)[x][1]['agerank'] >= agerank:
      if G.nodes(data=True)[x][1]['agerank'] != agerank:
        oldest = [] 
        agerank = G.nodes(data=True)[x][1]['agerank']
        oldest.append(G.nodes(data=True)[x][1])
        
    print G.nodes(data=True)[x][1]['label'],' %.2f' % all_degree_cent.get(x),\
    ' %.2f' % all_bet_cent.get(x),\
    ' %.2f' % all_close_cent.get(x)
  
  print "Oldest facebook(s): ", ', '.join([x['label'] for x in oldest])

  return names



G_lucas = nx.read_gml("/home/action/devdist/fb_lucas.gml")
G_igor = nx.read_gml("/home/action/devdist/fb_igor.gml")

G_lucas.name = "Facebook Lucas"
G_igor.name = "Facebook Igor"

l1 = print_info(G_lucas)
l2 = print_info(G_igor)
common = [val for val in l1 if val in l2]

suggestion = random.sample([val for val in l1 if not (val in common)], 3)

print "Mutual friends: " + ", ".join(common)
print "Number of mutual friends: " + str(len(common))
print "Suggestion of friends from lucas to igor (random criteria): " + ", ".join(suggestion)
