# 6. Lists
temperatures = [234,55,2352,3254,23,34]
#print(len(temperatures))
# [234,55,2352,3254,23,34]
# 0, 1, 2, 3, 4, 5
v0 = temperatures[0]
#print(v0)
temperatures_with_centi = [[245,2],[273,0]]
t1_c = temperatures_with_centi[1][0]
#print(t1_c)
t0,t1 = temperatures_with_centi
#print(t0)

# Exercise
# Create a 2 dimensional list of your favorites food, also with their taste type
fav_food = [['pay','sweet'],['soup','salty'],['chile','spicy']]
favorites_food = [fav_food[0][0],fav_food[1][0],fav_food[2][0]]
fav_tastes = [fav_food[0][1],fav_food[1][1],fav_food[2][1]]
print(fav_tastes)
