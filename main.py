




























if __name__ == '__main__':
	# Set up default puzzle
	puzzle = [[1,2,3],
			  [4,8,0],
			  [7,6,5]]

	# Intro message
	print 'Welcome to 861171527\'s 8-puzzle starter.'

	# Error handling variable
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
