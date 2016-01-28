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

finishing_time = {}

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

		if is_reverse == 1:
			for i in range(len(seen) - 1, -1, -1):
				t[0] += 1
				finishing_time[t[0]] = seen[i]

	explored = set()
	leader = {}
	n = len(G)
	t = [0]
	s = [0]
	i = n
	while i > 0:
		if is_reverse == 1:
			if i not in explored:
				dfs(i)
		elif is_reverse == 0:
			if finishing_time[i] not in explored:
				s[0] = i
				dfs(finishing_time[i])
				
		i -= 1
	#print 'finishing time: ' + str(finishing_time)
	#print 'leaders: ' + str(leader)
	print sorted(Counter(leader.values()).values())[-20:]

######################## Main ###############################
# Creating the reversed graph fot the first pass of the algorithm
from collections import defaultdict, Counter

graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file: 
	graph[int(line.split()[1])].add(int(line.split()[0]))
	print int(line.split()[1]), int(line.split()[0]) 

#graph = {1:{3}, 3:{2, 4}, 2:{1}, 4:{6}, 6:{5}, 5:{4}}

#SCC(graph, 1)

# Creating the graph fot the second pass of the algorithm
graph = defaultdict(set)
data_file = open("SCC.txt", "rb")
for line in data_file:
	graph[int(line.split()[0])].add(int(line.split()[1]))

#graph = {1:{2}, 2:{3}, 3:{1}, 4:{3,5}, 5:{6}, 6:{4}}
#SCC(graph, 0)


