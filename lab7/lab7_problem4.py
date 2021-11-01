# ESC180 Lab 7
# lab7_files_and_dict.py
# Oct 31, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# Problem 4

def get_phone_dict():
    s = open("data1_problem4.txt", encoding = "utf-8").read()
    lines = s.split("\n")
    lines2 = []
 
    for line in lines:
        if not (line.find(";;;")>=0):
            lines2.append(line)
    lines = lines2

    ph_class_dict = {}
    for line in lines:
        if len(line) < 3:
            continue
        phone, ph_class = line.split("  ")
        
        ph_class_dict[phone] = ph_class
        
    return ph_class_dict

print(get_phone_dict())