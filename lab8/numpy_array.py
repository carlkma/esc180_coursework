import numpy as np

# Problem 1
# print list of list as a np matrix
def print_matrix(M_lol):
	M = np.array(M_lol)
	print(M)

# Problem 2
# get index of first non-zero element in list row
def get_lead_ind(row):
	for i in range(len(row)):
		if row[i] != 0:
			return i
	return len(row)

# Problem 3
# get row with leading coefficient to the far left
def get_row_to_swap(M, start_i):
	val = []
	for i in range(start_i, len(M)):
		val.append(get_lead_ind(M[i]))
	return val.index(min(val)) + start_i

# Problem 4
# row operations
def add_rows_coefs(r1, c1, r2, c2):
	new_row = [0] * len(r1)
	for i in range(len(r1)):
		new_row[i] = r1[i] * c1 + r2[i] * c2
	return new_row

# Problem 5
# eliminate a coefficient with row operations
def eliminate(M, row_to_sub, best_lead_ind):
	for i in range(row_to_sub+1, len(M)):
		temp_row = add_rows_coefs(M[row_to_sub],-1*M[i][best_lead_ind],M[i],M[row_to_sub][best_lead_ind])
		M[i] = temp_row

# Problem 6
def forward_step(M):
	print("The matrix is currently:")
	print_matrix(M)
	print("Now performing the forward step")

	for row in range(len(M)):
		print("------------------------------------------------------------")
		print("Now looking at row " + str(row))
		n = get_row_to_swap(M, row)
		entry = get_lead_ind(M[n])

		print("Swapping rows %i and %i so that entry %i in the current row is non-zero" % (row,n,entry))
		M[row], M[n] = M[n], M[row]
		print("The matrix is currently:")
		print_matrix(M)

		print("Adding row %i to rows below it to eliminate coefficients in column %i" % (row,entry))
		eliminate(M, row, entry)
		print("The matrix is currently:")
		print_matrix(M)

	print("Done with the forward step")
	print("The matrix is currently:")
	print_matrix(M)

# Problem 7
def backward_step(M):
	print("The matrix is currently:")
	print_matrix(M)
	print("Now performing the backward step")

	new_M = M[::-1]

	for row in range(len(new_M)):
		print("------------------------------------------------------------")
		print("Now looking at row " + str(len(M) - 1 - row))
		eliminate(new_M, row, len(M) - 1 - row)
		print("The matrix is currently:")
		print_matrix(new_M[::-1])

	M = new_M[::-1]

	print("Now dividing each row by the leading coefficient")
	for i in range(len(M)):
		n = get_lead_ind(M[i])
		M[i] = [x/M[i][n] for x in M[i]]
	print("The matrix is currently:")
	print_matrix(M)

	# Return solutions as a list
	sol = []
	for i in M:
		sol.append(i[-1])
	return sol

# Problem 8 - Testing
# For Mx=b
# Given M
# Given b
# Find x
M = [[1, -2, 3, 22 ],
     [3, 10, 1, 314],
     [1, 5 , 3, 92 ],
     [1, 2 , 3, 4  ]]

b = [6,4,3,6]

def solve(M, b):
	for row in range(len(M)):
		M[row].append(b[row])
	forward_step(M)
	sol = backward_step(M)
	return sol
sol = solve(M, b)
print()
print("THE SOLUTION IS:")
print(sol)
print()


# Verification
# Given M
# Given x
# Check b
# Testing whether or not Mx = b
print("Verifying the input value of b:")
M = np.array([[1, -2, 3, 22],[3, 10, 1, 314],[1, 5, 3, 92],[1,2,3,4]])
x = np.array(sol)
b = np.matmul(M,x)        
print(b)