# ESC180 Notes

# Swap var without temp var or multi assignment
a = 1
b = 2
a = a+b # compute sum
b = a-b # b = a
a = a-b # a = b

#xor
a1 = True
a2 = False
a1 + a2 == 1

(a1 or a2) and not (a1 and a2)

a1 != a2

a1 ^ a2

# ---------- ------- ---------- #
# ---------- Week 07 ---------- #
# ---------- ------- ---------- #

# exec
s = "a = 42\nprint(a+1)\n"
print(s)
exec(s)

# tuples
t = (1,2,3,4)
t[0] = 5 # Error; tuples are immutable
t = ([1,2],2,3,4) # can include mixed types

# dictionaries
grades = {"PHY": 90, "CSC": 85, "CIV": 100, "ESC": 85}
grades["CSC"] = 84 # modify values
grades["MAT"] = 87 # add entries

L = [1, 2]
grades[L] = 5 # Error; keys are immutable

a = {"a320":4,"b737":19,"cs100":2}
print(a["cs100"]) # 2
print(list(a.items())) # [('a320', 4), ('b737', 19), ('cs100', 2)]



# ---------- ------- ---------- #
# ---------- Week 08 ---------- #
# ---------- ------- ---------- #


# open & read file
f = open("in.txt", encoding="latin1")
s = f.read()
f.close()