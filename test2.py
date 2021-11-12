#1
print("Krystle Berry")
#2 a for loop
for i in range(start, end + 1):
    print(i)

### Work with files
# 3 read notes.txt files and count the line on it
file_read = open("notes.txt", "r") #mode r = read
all_lines = file_read.readlines()
print(f"There are {len(all_lines)} line in the file") # stinrg formatting
file_read.close()


#create a new file
test = open("demo.txt", "w") #mode w = write
test.write ("Hwllo from python\n")
test.write("this should be a second line\n")
test.write("\n")
test.close()



#Write a line in the bottom of notes.txt
notes = open("notes.txt", "a")
notes = write("\n***This text was added with Python code")
notes.close()