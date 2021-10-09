# ESC180 Lab 4
# loops_and_pi.py
# Oct 5, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)
import math


# Problem 1
def count_evens(L):
	s = 0
	for num in L:
		if num % 2 == 0:
			s += 1
	return s


# Problem 2
def list_to_str(lis):
	s = "["
	for num in lis:
		s += str(num) + ", "
	s = s.rstrip(", ")
	s += "]"
	return s

def lists_are_the_same(list1, list2):
	if len(list1) == len(list2):
		for i in range(len(list1)):
			if list1[i] == list2[i]:
				continue
			else:
				return False
	else:
		return False
	return True

steps1 = [0]
def simpify_fraction(n, m):
	big = max(n,m)
	for i in range(big, 0, -1):
		n1 = n / i
		m1 = m / i
		steps1[0] += 1
		if n1 == int(n1) and m1==int(m1):
			return str(int(n1)) + "/" + str(int(m1))
	return str(n) + "/" + str(m)

def count_terms(n):
	sum = 0
	i = 0
	while True:
		sum += (-1)**i/(2*i+1)
		i+=1
		pi = 4* sum
		if int(pi*(10**(n-1))) == int(math.pi*(10**(n-1))):
			print(pi)
			return i

steps2 = [0]
def euclid(n, m):
	if n==0:
		return m
	steps2[0] += 1
	return euclid(m % n, n)

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = [2,3,4,5,1]
print("Problem 1")
print(count_evens(a))
print()


print("Problem 2")
print(list_to_str(a))
print()


print("Problem 3")
print(lists_are_the_same(a,b))
print(lists_are_the_same(a,c))
print()


print("Problem 4")
print(simpify_fraction(1, 2))
print(simpify_fraction(16, 12))
print()


print("Problem 5")
print(count_terms(5))
print()


print("Problem 6")
steps1 = [0]
steps2 = [0]
print(simpify_fraction(2322,654))
print(euclid(2322,654))
print(steps1[0], steps2[0])