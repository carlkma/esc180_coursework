# ESC180 Lab 3 Problem 1
# test_calc.py
# Sept 27, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

import lab02

if __name__ == '__main__':
    lab02.initialize()
    lab02.subtract(4)
    
    if lab02.get_current_value() == -535:
      print("Test 1 passed")
    else:
      print("Test 1 failed")