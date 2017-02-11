from Node import Node
from heapq import heapify, heappush, heappop
import copy

# Globally set, final puzzle state to be used in methods
final_state = [[1,2,3],
			   [4,5,6],
			   [7,8,0]]

def misplaced(problem):
	""" 
	Counts total misplaced tiles in the puzzle, 
	returns as the heuristic value.
	"""
	heuristic = 0
	for i in range(3):
		for j in range(3):
			if problem[i][j] != 0:
				if problem[i][j] != final_state[i][j]:
					heuristic += 1

	return heuristic

def manhattan(problem):
	"""
	Returns the total manhattan distance in the puzzle.
	Manhattan distance formula = abs(x1 - x0) + abs(y1 - y0)
	"""
	heuristic = 0

	# The range of the first for loop == all the numbers in the puzzle
	# i.e. in the 8-puzzle we have 1-8 --> for x in range(1,9)
	# if puzzle is changed, change the range accordingly
	for x in range(1,9):
		for i in range(3):
			for j in range(3):
				# We obtain the row and col of the curr state and final state
				# then calculate the distance between them, and add it to heuristic
				if x == problem[i][j]:
					problemRow = i
					problemCol = j
				if x == final_state[i][j]:
					finalRow = i 
					finalCol = j
		heuristic += (abs(problemRow - finalRow) + abs(problemCol - finalCol))
	return heuristic

def expand(currNode, nodes_expanded):
	"""
	This method expands the current node by getting performing the operations
	(left, right, up, down) on the puzzle and also updates the total
	number of nodes expanded. Both results are returned: list, nodes_expanded
	"""

	# Empty list to store the new nodes
	# depth to update
	List = []
	depth = currNode.depth + 1
	# find location of '0' in the puzzle
	blankRow = 0
	blankCol = 0
	for i in range(3):
		for j in range(3):
			if currNode.puzzle_state[i][j] == 0:
				blankRow = i 
				blankCol = j
				print i, j 


	# copies the puzzle, and then determines/swaps with tile if possible
	# need deepcopy or it will be referenced
	# ^Info found on: stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list

	# TOP
	if blankRow != 0:
		top = copy.deepcopy(currNode.puzzle_state)
		# replace the 0 with the value above it
		top[blankRow][blankCol] = top[blankRow - 1][blankCol]
		# value above it now holds the value 0
		top[blankRow - 1][blankCol] = 0
		# create node object, append to the list
		topNode = Node(0, depth, top)
		print 'top: ' , top
		List.append(topNode)
		nodes_expanded += 1

	# BOT
	if blankRow != 2:
		bot = copy.deepcopy(currNode.puzzle_state)

		bot[blankRow][blankCol] = bot[blankRow + 1][blankCol]

		bot[blankRow + 1][blankCol] = 0

		botNode = Node(0, depth, bot)
		List.append(botNode)
		print 'bot: ' , bot
		nodes_expanded += 1

	# LEFT
	if blankCol != 0:
		left = copy.deepcopy(currNode.puzzle_state)

		left[blankRow][blankCol] = left[blankRow][blankCol - 1]

		left[blankRow][blankCol - 1] = 0

		leftNode = Node(0, depth, left)
		List.append(leftNode)
		print 'left: ' , left
		nodes_expanded += 1

	# RIGHT
	if blankCol != 2:
		right = copy.deepcopy(currNode.puzzle_state)

		right[blankRow][blankCol] = right[blankRow][blankCol + 1]

		right[blankRow][blankCol + 1] = 0

		rightNode = Node(0, depth, right)
		List.append(rightNode)
		print 'right: ' , right
		nodes_expanded += 1



	return List, nodes_expanded




def searchAlgorithm(problem, choice):
	"""
	Uniform Cost Search, misplaced tile search, and manhattan distance
	search are all contained in this method. 
	choice determines the search method used, while problem is the
	initial puzzle state that needs to be solved
	"""
	# Set up data/storage needed for algorithm
	# i.e create node object with correct heuristics, depth and heapq
	# IMPORTANT: depth = cost for this puzzle solution --> g(n) = depth level
	nodes_expanded = 0
	max_queue_nodes = 0

	if choice == 1:
		init_node = Node(0, 0, problem)

	if choice == 2:
		# Get heuristic for misplaced tile

		h = misplaced(problem)
		init_node = Node(h,0, problem)

	if choice == 3:
		# Get heuristic for manhattan distance
		h = manhattan(problem)
		init_node = Node(h, 0, problem)
	# Push the node to the priority queue
	pq = []
	heappush(pq, init_node)
	print len(pq)

	# Begin loop
	goal = False

	while not goal:

	# Make temp node = current node in front of queue & pop
		heapify(pq)
		temp_node = heappop(pq)
		print temp_node.puzzle_state

	# check if temp node = solution, if it is -> print and exit loop
		if temp_node.puzzle_state == final_state:
			goal = True
			print 'Goal!'
			print temp_node.puzzle_state
			print 'To solve this problem the search algorithm expanded a total of ' , nodes_expanded , 'nodes.'
			print 'The maximum number of nodes in the queue at any one time was ' , max_queue_nodes , '.'
			print 'The depth of the goal node was ' , temp_node.depth , '.'

	# else, expand node (swap up,down,left,right) || expand method returns list of nodes and nodes_expanded
	# during expansion, update nodes_expanded --> expand(temp_node, nodes_expanded)
		else:
			tempList, nodes_expanded = expand(temp_node, nodes_expanded)


	# push the children nodes into the queue, and use heappush/heapify to sort by priority
	# also update the heuristics to correct one
			for x in range(len(tempList)):
				if choice == 1:
					tempList[x].heuristic = 0
				if choice == 2:
					tempList[x].heuristic = misplaced(tempList[x].puzzle_state)
				if choice == 3:
					tempList[x].heuristic = manhattan(tempList[x].puzzle_state)

				heappush(pq, tempList[x])
	# update max_queue_nodes
			if max_queue_nodes < len(pq):
				max_queue_nodes = len(pq)











if __name__ == '__main__':
	# Set up default puzzle
	puzzle = [[1,2,3],
			  [4,8,0],
			  [7,6,5]]

	# Intro message
	print 'Welcome to 861171527\'s 8-puzzle starter.'

	# Determines when the menu loops stop
	menu = True

	# Getting user input and setting up correct puzzle
	while menu:
		print 'Type "1" to use a default puzzle, or "2" to enter your own puzzle.'
		choice = raw_input()
		if choice == "1":
			# Do nothing, default puzzle already created 
			menu = False
		elif choice == "2":
			print 'Enter your puzzle, use a zero to represent the blank'
			print 'Enter the first row, use space or tabs between numbers'

			a,b,c = raw_input().split()
			puzzle[0][0] = int(a)
			puzzle[0][1] = int(b)
			puzzle[0][2] = int(c)

			print 'Enter the second row, use space or tabs between numbers'

			a,b,c = raw_input().split()
			puzzle[1][0] = int(a)
			puzzle[1][1] = int(b)
			puzzle[1][2] = int(c)

			print 'Enter the third row, use space or tabs between numbers'
			a,b,c = raw_input().split()
			puzzle[2][0] = int(a)
			puzzle[2][1] = int(b)
			puzzle[2][2] = int(c)
			print puzzle	
			menu = False
		else:
			print 'Invalid choice. Try again.'

	# Prompt user to pick an algorithm to solve the puzzle
	while not menu:
		print 'Enter the choice of your algorithm'
		print '1. Uniform Cost Search'
		print '2. A* with the Misplaced Tile heuristic'
		print '3. A* with the Manhattan distance heuristic'

		choice = raw_input()

		if choice == "1":
			searchAlgorithm(puzzle, 1)
			menu = True
		elif choice == "2":
			searchAlgorithm(puzzle, 2)
			menu = True
		elif choice == "3":
			searchAlgorithm(puzzle, 3)
			menu = True
		else:
			print 'Invalid choice. Try again.'
