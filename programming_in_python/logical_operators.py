# 11. Logical operators
"""
- AND
--------------------------------
1st value | 2nd value | output |
--------------------------------
True      | True      | True   |
--------------------------------
True      | False     | False  |
--------------------------------
False     | True      | False  |
--------------------------------
False     | False     | False  |
--------------------------------

- OR
--------------------------------
1st value | 2nd value | output |
--------------------------------
True      | True      | True   |
--------------------------------
True      | False     | True   |
--------------------------------
False     | True      | True   |
--------------------------------
False     | False     | False  |
--------------------------------

- NOT
--------------------
1st value | output |
--------------------
True      | False  |
--------------------
False     | True   |
--------------------
"""
# AND
#print(True and True)
#print(True and False)
#print(False and False)
#print(False and True)

# OR
#print(True or True)
#print(True or False)
#print(False or True)
#print(False or False)

# NOT
#print(not (True or False or False))

num = int(input("input a number: "))
if (num %2 == 0) and (num > 200):
    print("number is greater than 200 and even")
else :
    print("the number is less than 200 or the number is odd or both")
