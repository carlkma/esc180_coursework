# ESC180 Lab 3 Problem 2-3
# problem2&3.py
# Sept 27, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# Problem 2

def implementation1(n):
	sum = 0
	for i in range(1,n+1):
		sum += i**3
	return sum

def implementation2(n):
	sum = 0
	for i in range(1,n+1):
		sum += i
	return sum**2

def check_sum(n):
	if implementation1(n) == implementation2(n):
		return True
	else:
		return False

def check_sums_up_to_n(N):
	for i in range(N+1):
		if check_sum(i) == False:
			return False
	return True


print(implementation1(5))
print(implementation2(5))
print(check_sum(5))
print(check_sums_up_to_n(100))


# Problem 3
sum = 0
for i in range(1001):
	sum += (-1)**i/(2*i+1)
print(sum)
print(sum * 4)