# Reza Asad
# Algorithm Class
# Jan 24th, 2016
######################### Algorithms ######################
# Implementation of the strongly conncected components of 
# a directed graph using Kosaraju's algorithm
# input: 
#	G: A dictionary representing a directed graph
#	reverse: A boolean to indicate weather the input
#		graph is the original graph or if it is reversed
# output:
#	leader: The strongly connected componets of the graph
explored = set()
finishing_time = {}
leader = {}
def SCC(G, reverse):
	t = 0
	n = len(G.keys())
	for i in range(n, -1, -1):
		if i not in explored:
			if reverse == 0:
				s = i
			dfs(G, i)
	def dfs(G, i):
		explored.add(i)
		if reverse == 0:
			leader[i] = s
		for j in G[i]:
			if j not in  explored:
				dfs(G, j)
		
		if reverse == 1:
			t += 1
			finishing_time[i] = t




######################## Main ###############################
# Creating the reversed graph fot the first pass of the algorithm
from collections import defaultdict

graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file:
	graph[int(line.split()[1])].add(int(line.split()[0]))

SCC(graph, 1)

# Creating the graph fot the second pass of the algorithm
graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file:
	graph[int(line.split()[0])].add(int(line.split()[1]))

SCC(graph, 0)



