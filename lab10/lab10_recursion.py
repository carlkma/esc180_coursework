# ESC180 Lab 10
# lab10_recursion.py
# Dec 3, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# Problem 1
print("Problem 1")
# return x raised to the power of n
def power(x,n):
    if n == 1:
        return x
    else:
        return x * power(x,n-1)
print(power(3,3))
print(power(-3,3))



# Problem 2
print()
print("Problem 2")
# return lists L1 and L2 interleaved
def interleave(L1,L2):
    if len(L1) == len(L2) == 0:
        return L1
    else:
        l1 = L1.pop(0)
        l2 = L2.pop(0)
        return [l1, l2] + interleave(L1,L2)
L1 = [1,3,5,7,9]
L2 = [2,4,6,8,10]
print(interleave(L1,L2))



# Problem 3
print()
print("Problem 3")
def reverse_rec1(L):
    if len(L)==0:
        return []
    else:
        return [L[-1]] + reverse_rec1(L[:-1])
L2 = [2,4,6,8,10]
L2 = reverse_rec1(L2)
print(L2)


def reverse_rec2(L,idx):
    if idx==len(L)//2:
        return
    else:
        L[idx], L[-1-idx] = L[-1-idx], L[idx]
        idx+=1
        reverse_rec2(L,idx)
        
L2 = [2,4,6,8,10]
reverse_rec2(L2,0)
print(L2)




# Problem 4
print()
print("Problem 4")
def zigzag(L):
    if len(L) % 2 != 0:
        print(L[len(L)//2], end=" ")
        L = L[:len(L)//2] + L[len(L)//2+1:]
        zigzag(L)
    elif len(L) == 2:
        print(L[0],L[1])
    else:
        print(L[len(L)//2-1], L[len(L)//2], end = " ")
        L = L[:len(L)//2-1]+L[len(L)//2+1:]
        zigzag(L)
a = [1,2,3,4,5,6,7,8,9]
zigzag(a)



# Problem 5
print()
print("Problem 5")

def is_balanced(s):
    temp = check(s)
    if temp == 0:
        return False
    elif temp == 1:
        return True
    else:
        return is_balanced(temp)

def check(s):
    if s.find("(") == -1 and s.rfind(")") == -1:
        return 1
    elif s.find("(") == -1 or s.rfind(")") == -1:
        return 0
    else:
        s = s.replace("(","",1)
        s = s.replace(")","",1)
        
        return s

print(is_balanced("(asdf)()()(((((("))


print()
print("Problem 6")
print("Thank you!")