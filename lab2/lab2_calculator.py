# ESC180 Lab 2
# calculator.py
# Sept 23, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

stack = []

def display_current_value():
	global current_value, count 
	print("Current value: " + str(current_value))
	stack.append(current_value)

def add(to_add):
	global current_value
	current_value += to_add

def multiply(num):
	global current_value
	current_value *= num

def divide(num):
	global current_value
	if num != 0:
		current_value /= num
	else:
		#raise ZeroDivisionError
		print("Zero Division Error")

def save():
	global current_value
	with open('tmp.txt', 'w') as file:
		file.write(str(current_value))

def recall():
	global current_value
	with open('tmp.txt', 'r') as file:
		current_value = float(file.readline())

def undo():
	global current_value
	if len(stack) > 1:
		previous = stack.pop() # restores the previous value displayed on screen
		#previous = current_value # restores the previous value calculated by processor
		current_value = stack.pop() 
		stack.append(previous) # comment out for full undo history
	display_current_value()
	

if __name__ == "__main__":
	current_value = 0
	previous = 0

	# Problem 1
	print("Problem 1")
	print("Welcome to the calculator program.")
	print("Current value: " + str(current_value))
	print()

	# Problem 2
	print("Problem 2")
	display_current_value()
	print()

	# Problem 3
	print("Problem 3")
	add(5)
	display_current_value()
	print()

	# Problem 4
	print("Problem 4")
	print("If current_value is not declared global, it would be a local (and undefined) variable")
	print()

	# Problem 5
	print("Problem 5")
	multiply(5)
	display_current_value()
	divide(5)
	display_current_value()
	divide(0)
	print()

	# Problem 6
	print("Problem 6")
	save()
	current_value = 999
	recall()
	display_current_value()
	print()

	# Problem 7
	print("Problem 7")
	add(10)
	display_current_value()
	add(10)
	add(10)
	add(10)
	display_current_value()
	#print(stack)
	undo()
	undo()