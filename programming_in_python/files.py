# 16. File handling
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
    file = open(file_name, "r")
    stuff = file.read()
    print(stuff)
    file.close() # ← always close the file

#read_file("apples.txt") # ← take care of the existence of the file

# append, "a"
def append_file(file_name, stuff):
    file = open(file_name, "a")
    file.write(stuff)
    file.close()

append_file("apples.txt", ", really something is definitely up")
read_file("apples.txt")
