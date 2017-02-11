class Node:
	""" 
	This class contains the instance variables that
	describe the state space of the problem.
	"""
	# Problem object is initialized with data when created
	# initial and final are 2d arrays, operators is a list
	# of the operations for the problem.
	def __init__(self, heuristic, depth, puzzle):
		self.heuristic = heuristic
		self.depth = depth
		self.puzzle_state =  puzzle
		self.cost = heuristic + depth

	# Allows heapify/heappush to compare the total cost of two nodes
	def __cmp__(self, other):
		return cmp(self.cost, other.cost)
		
	# Operators for the 8 puzzle problem

	# swap blank with number above


	# swap blank with number below


	# swap blank with number to the left


	# swap blan with number to the right