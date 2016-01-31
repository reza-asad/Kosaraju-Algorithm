# Reza Asad
# Algorithm Class
# Jan 24th, 2016
######################### Algorithms ######################
# Implementation of the strongly conncected components of 
# a directed graph using Kosaraju's algorithm
# input: 
#   G: A dictionary representing a directed graph
#   is_reverse: A boolean to indicate weather the input
#       graph is the original graph or if it is reversed
#   num_nodes: The number of nodes of the graph
#
# output:
#   leader: The strongly connected componets of the graph
#
# Note: it is assumed that the graphs are labled from 1 to 
# num_nodes
finishing_time = {}
t = [0]
s = [0]

def SCC(G, is_reverse, max_node_label):
    def dfs(G, i):
        stack = []
        seen = []
        stack.append(i)
        while stack:
            v = stack.pop()
            if v not in explored:
                explored.add(v)
                seen.append(v)
                leader[v] = s[0]
                stack.extend(G[v] - explored)

        if is_reverse == 1:
            for i in range(len(seen) - 1, -1, -1):
                t[0] += 1
                finishing_time[t[0]] = seen[i]

    explored = set()
    leader = {}
    i = num_nodes
    while i > 0:
        if is_reverse == 1:
            if i not in explored:
                dfs(G, i)
        elif is_reverse == 0:
            if finishing_time[i] not in explored:
                s[0] = finishing_time[i]
                dfs(G, finishing_time[i])
                
        i -= 1
    print sorted(Counter(leader.values()).values())[-5:]

######################## Main ###############################
# Creating the reversed graph fot the first pass of the algorithm.
# The ordering of the second pass is determined during this pass.
from collections import defaultdict, Counter

graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file: 
        graph[int(line.split()[1])].add(int(line.split()[0]))

SCC(graph, 1, 875714)

# Creating the original graph for the second pass of the algorithm.
# The graph is traversed using the ordering computed in the first pass.
graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file:
    graph[int(line.split()[0])].add(int(line.split()[1]))

SCC(graph, 0, 875714)

