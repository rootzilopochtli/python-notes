# 17. Error handling
#file = open("apples.txt", "w")
# modes
# write, "w"
def write_file(file_name, stuff):
    file = open(file_name, "w")
    file.write(stuff)
    file.close()

#write_file("apples.txt", "Yo nothing is upp")

# read, "r"
def read_file(file_name):
    # error handling ↓ (take care of identation)
    try:
        file = open(file_name, "r")
        stuff = file.read()
        print(stuff)
        file.close() # ← always close the file
    except:
        #print("something seriously went wrong with reading file")
        print("The file " + file_name + " doesn't exist")

#read_file("apples.txt") # ← take care of the existence of the file

# append, "a"
def append_file(file_name, stuff):
    file = open(file_name, "a")
    file.write(stuff)
    file.close()

#append_file("apples.txt", ", really something is definitely up")
#read_file("apples.txt")

password = "1234567"
if len(password) < 10:
    raise Exception("The password must be greater than 10")
