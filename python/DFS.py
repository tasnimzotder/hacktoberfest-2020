# DFS Traversal Function
def dfs(l, start_node, goal_node):
	visited = [0]*10
	visited[start_node] = 1
	print('DFS : ', end = " ")
	print(start_node, end = " ")
	s = []
	while start_node != goal_node:
		p = -1
		for i in l[start_node]:
			k = 0
			p += 1
			if i == 1 and visited[p] != 1:
				k += 1
				visited[p] = 1
				s.append(start_node)
				start_node = p
				print('-->', end = " ")
				print(start_node, end = " ")
				break
		if k == 0:
			start_node = s.pop()

## main program

# Graph Declaration
l = [[0,0,0,1,0,1,1,0,1,1],
     [0,0,1,1,1,1,1,1,0,1], 
     [0,1,0,0,1,1,0,1,1,1], 
     [1,1,0,0,0,0,1,0,0,0], 
     [0,1,1,0,0,0,1,0,1,1], 
     [1,1,1,0,0,0,1,0,0,1], 
     [1,1,0,1,1,1,0,1,0,1], 
     [0,1,1,0,0,0,1,0,1,1], 
     [1,0,1,0,1,0,0,1,0,0], 
     [1,1,1,0,1,1,1,1,0,0]]

# DFS Traversal
start_node = 0
goal_node = 4
dfs(l, start_node, goal_node)
print()
