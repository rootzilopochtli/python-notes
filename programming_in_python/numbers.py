# 4. Numbers
integer_number = 17
float_number = 17.44444
complex_num = 17j + 23 # not discuss
x = 87
y = 42
addition = x + y
subtraction = x - y
multiplication = x * y
pure_division = x / y
# print(pure_division)
# integer division
floor_division = x // y # 2
# print(floor_division)
mod = x % y
# 87 // 42 , 2*42 = 84... remainder 3
# print(mod) # 42 // 87
# print(42 % 87)
"""
The result of floor_division is the integer of the division and the mod is the remainder.
87/42=2 remainder 3 → 42*2=84+3=87
floor(//)
mod(%)
"""
# exponential
# 2^2.. 2x2 .. 2^3 .. 2x2x2
expo = x ** y
# print(expo)

"""
Exercise
"""
# Exercise 1
# 5 % 10
num1 = 5
num2 = 10
mod1 = num1 % num2
#print(mod1) # ✓

# Exercise 2
# 5 // 2
num3 = 2
floor_division1 = num1 // num3
#print(floor_division1) # ✓

# Exercise 3
# 70 // 30
num4 = 70
num5 = 30
floor_division2 = num4 // num5
#print(floor_division2) # ✓

# Exercise 4
# 53 % 7
num6 = 53
num7 = num1 + num3
mod2 = num6 % num7
#print(mod2) # ✓

# Exercise 5
# 34 / 23
num8 = num5 + num3 + num3
num9 = num2 + num2 + num1 - num3
div = num8 / num9
#print(div) # ✓

# Exercise 6
# 4 ** 2
num10 = num3 + num3
exp1 = num10 ** num3
#print(exp1) # ✓
