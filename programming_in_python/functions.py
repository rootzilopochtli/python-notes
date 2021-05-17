# 13. Functions
#def fun_name():
#    print("You called me")
#fun_name()
def fun_name(param1, param2, param3):
    x = param1 * 23
    param3 = param3*99
    value = param1 + param2 + param3
    return value
x = fun_name(2,33,34)
#print(x)

def is_even (num):
    if (num % 2) == 0:
        return True
    else :
        return False
    print("anything")
#print( is_even(2) )

# optional
# recursion
def count_down(x):
    if x == 1 :
        #print(x)
        return 1
    #print(x)
    return count_down(x-1)
count_down(9)
"""
# lambda expressions - anonymous
>>> lam = lambda arg1 : arg1 * 2
>>> lam(2)
4
>>> lam(545)
1090
"""

# Function that calculate the length of a string (extra length of a string)
def calculate_len(s):
    i = 0 ;
    while(i < len(s)):
        i = i + 1
    return i
#print(calculate_len("sasdasD"))
