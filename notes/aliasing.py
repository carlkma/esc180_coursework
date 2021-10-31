# ------------------------------

def f():
    L[0] = 0
    L = [4,5,6]

L = [1,2,3]
f() # UnboundLocalError: local variable 'L' referenced before assignment
print(L) # NO OUTPUT

# ------------------------------

def f(L):
    L[0] = 0
    # Note: inner id(L) == outer id(L)
    L = [4,5,6]
    # Note: inner id(L) changed

L = [1,2,3]
f(L)
print(L) # [0, 2, 3]

# ------------------------------

L = [[1,2],3]
M = L[:]
M[0][1] = 5
M[1] = 5
print(L) # [[1, 5], 3]

# Note: id(L) != id(M) but
# Note: id(L[0]) == id(M[0]) and id(L[1]) == id(M[1])
# Note: use new_M = [ x[:] for x in M ]

# ------------------------------
