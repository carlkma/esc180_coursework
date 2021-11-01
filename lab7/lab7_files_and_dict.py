# ESC180 Lab 7
# lab7_files_and_dict.py
# Oct 31, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# Problem 1
f = open("data2.txt")
text = f.read()
f.close()

lines = text.split("\n")
print("Problem 1")

for line in lines:
    if line.lower().find("lol")>=0:
        print(line)
print()

# Problem 2
def dict_to_str(d):

    '''Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).'''
    result = ""
    for key, value in d.items():
        result += f"{key}, {value}"
        result += "\n"
    return result.strip()
print("Problem 2")
print(dict_to_str({"a320":4,"b737":19,"cs100":2}))
print()


# Problem 3
def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    in ascending order."""
    
    keys = sorted(list(d.keys()))
    result = ""
    for key in keys:
        result += f"{key}, {d[key]}"
        result += "\n"
    return result.strip()

print("Problem 3")
print(dict_to_str_sorted({"f18":3,"a320":4,"b737":19,"cs100":2}))
print()
