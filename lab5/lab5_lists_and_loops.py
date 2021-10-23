# ESC180 Lab 5
# lab5_lists_and_loops
# Oct 15, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# Problem 1
def list1_starts_with_list2(list1, list2):
    if len(list1) >= len(list2):
        #if list1[:len(list2)]==list2:
        #   return True
        temp = False
        for i in range(len(list2)):
            if list1[i] == list2[i]:
                temp = True
            else:
                return False
    if temp == True:
        return True
    return False

list1 = [2,1,4,6,7,8]
list2 = [2,3,4]
print("Problem 1")
print(list1_starts_with_list2(list1,list2))
print()



# Problem 2
def match_pattern(list1, list2):
    if len(list1) < len(list2):
        return False

    for i in range(len(list1) - len(list2) + 1):
        if list1[i:(i+len(list2))] == list2:
            return True
    return False

list1 = [4, 10, 2, 5, 50, 100]
list2 = [2, 3, 50]
print("Problem 2")
print(match_pattern(list1,list2))
print()


# Problem 3
def repeats(list0):
    if len(list1) > 1:
        for i in range(len(list0)-1):
            if list0[i] == list0[i+1]:
                return True
    return False
list0 = [3,13,4,6,8,9]
print("Problem 3")
print(repeats(list0))
print()


# Problem 4a
def print_matrix_dim(M):
    print(str(len(M))+"x"+str(len(M[0])))
M = [[1,2],[3,4],[5,6]]
print("Problem 4a")
print_matrix_dim(M)
print()



# Problem 4b
def mult_M_v(M, v):
    product = []
    for i in range(len(M)):
        temp_row = 0
        for j in range(len(M[0])):
            temp_row += M[i][j] * v[j]
        product.append(temp_row)
    return product
print("Problem 4b")
a = [[1,2],[3,4],[5,7]]
b = [1,2]
print(mult_M_v(a,b))
print()



# Problem 4c
def dot_product(v1, v2):
    product = 0
    for i in range(len(v1)):
        product += v1[i] * v2[i]
    return product

def matrix_multiplication(M1,M2):
    new_matrix = []
    for row_of_m1 in range(len(M1)):
        new_row = []
        for col_of_m2 in range(len(M2[0])):

            new_row.append(dot_product(M1[row_of_m1], [item[col_of_m2] for item in M2]))
            
        new_matrix.append(new_row)
    return new_matrix

print("Problem 4c Test 1")
a = [[1,2,3],[4,5,6]]
b = [[7,8],[9,10],[11,12]]
print(matrix_multiplication(a,b))
print()
print("Problem 4c Test 2")
a = [[3,4,2]]
b = [[13,9,7,15],[8,7,4,6],[6,4,0,3]]
print(matrix_multiplication(a,b))