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
import sys
sys.setrecursionlimit(15000)

finishing_time = {}
leader = {}

def SCC(G, is_reverse):
	def dfs(i):
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

		for i in range(len(seen) - 1, -1, -1):
			t[0] += 1
			finishing_time[t[0]] = seen[i]

	explored = set()
	n = len(G)
	t = [0]
	s = [0]
	i = n
	while i > 0:
		if i not in explored:
			if is_reverse == 0:
				s[0] = i
				dfs(finishing_time[i])
			else:
				dfs(i)
		i -= 1


######################## Main ###############################
# Creating the reversed graph fot the first pass of the algorithm
#from collections import defaultdict

#graph = defaultdict(set)
#data_file = open("SCC.txt", "rb")
#for line in data_file:
#	graph[int(line.split()[1])].add(int(line.split()[0]))

#SCC(graph, 1)

# Creating the graph fot the second pass of the algorithm
#graph = defaultdict(set)
#data_file = open("SCC.txt", "rb")
#for line in data_file:
#	graph[int(line.split()[0])].add(int(line.split()[1]))

#SCC(graph, 0)


graph = {1:{7}, 4:{1}, 7:{4, 9}, 9:{6}, 6:{3, 8}, 3:{9}, 8:{2}, 2:{5}, 5:{8}}

SCC(graph, 1)
print finishing_time

graph = {7:{1}, 4:{7}, 1:{4}, 9:{3, 7}, 6:{9}, 3:{6}, 8:{5, 6}, 5:{2}, 2:{8}}
SCC(graph, 0)
print leader
