class Node:
	""" 
	This class contains the instance variables that
	describe the state space of the problem.
	"""
	# Problem object is initialized with data when created
	# initial and final are 2d arrays, operators is a list
	# of the operations for the problem.
	def __init__(self, heuristic, depth, initial):
		self.heuristic = heuristic
		self.depth = depth
		self.puzzle_state = initial
		
	# Operators for the 8 puzzle problem

	# swap blank with number above


	# swap blank with number below


	# swap blank with number to the left


	# swap blan with number to the right