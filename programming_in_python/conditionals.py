# 9. Conditionals
is_the_door_open = False
is_the_light_on = True
is_password_valid = True
#
if is_password_valid:
    #print("password is valid")
else :
    #print("Your password is not valid")
    # if else chaining
if is_the_light_on:
    print("The light is on")
elif is_the_door_open:
    print("The door is open, but light is off")
else :
    print("the ligth is not on, the door is not open")
