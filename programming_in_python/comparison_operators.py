# 10. Comparison operators
# compare
n1 = 5
n2 = 10
# greater than
n1_gt_n2 = n1 > n2 # return a boolean
#print(n1_gt_n2)
# less than
n1_lt_n2 = n1 < n2
#print(n1_lt_n2)
#print(83 < 120)
# greater than eqal
#print(n1 >= n2)
#print(99 >= 99)
# less than eqal
#print(5 <= 5)
# not eqal to
#print( 5 != 9 )
# eqal to
#print(n1 == 5)
password = input("password: ")
# 123456 = correct
correct_pass = "123456"

#if password == correct_pass:
if len(password) >= 6 :
    #print("correct password")
    print("nice length")
else :
    #print("incorrect password")
    print("to short password")
