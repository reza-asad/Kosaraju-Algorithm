# Reza Asad
# Algorithm Class
# Jan 24th, 2016
######################### Algorithms ######################
# Implementation of the strongly conncected components of 
# a directed graph
explored = set()
finishing_time = {}
leader = {}
def SCC(G, forward):
	n = len(G.keys())
	for i in range(n, -1, -1):
		if i not in explored:
			dfs(G, i)
	def dfs(G, i):
		if forward == 1:
			pass
		else:
			pass
######################## Main ###############################
# Creating the reversed graph fot the first pass of the algorithm
from collections import defaultdict

graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file:
	graph[int(line.split()[1])].add(int(line.split()[0]))

SCC(graph, 0)

# Creating the graph fot the second pass of the algorithm
graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file:
	graph[int(line.split()[0])].add(int(line.split()[1]))

SCC(graph, 1)