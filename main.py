from Node import Node
from heapq import heapify, heappush, heappop

# Globally set, final puzzle state to be used in methods
final_state = [[1,2,3],
			   [4,5,6],
			   [7,8,0]]

def misplaced(problem):
	""" 
	Counts total misplaced tiles in the puzzle, 
	returns as the heuristic value
	"""
	heuristic = 0
	for i in range(3):
		for j in range(3):
			if problem[i][j] != 0:
				if problem[i][j] != final_state[i][j]:
					heuristic += 1

	return heuristic





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
	if choice == 1:
		init_node = Node(0, 0, problem)

	if choice == 2:
		# Get heuristic for misplaced tile

		init_node = Node(0,0, problem)

	if choice == 3:
		# Get heuristic for manhattan distance
		init_node = Node(0, 0, problem)
	# Push the node to the priority queue

	# Begin loop

	# If queue length = 0, exit

	# Make temp node = current node in front of queue

	# pop node from queue

	# check if temp node = solution

	# if true, exit loop

	# else, expand node (swap up,down,left,right)

	# push the children nodes into the queue, and use heapify to auto sort









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
			print 'UCS method'
			menu = True
		elif choice == "2":
			searchAlgorithm(puzzle, 2)
			print 'misplaced tile heuristic method'
			menu = True
		elif choice == "3":
			searchAlgorithm(puzzle, 3)
			print 'manhattan distance heuristic method'
			menu = True
		else:
			print 'Invalid choice. Try again.'
