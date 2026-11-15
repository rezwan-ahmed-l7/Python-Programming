''' 
r = read
w = overwrite & r+ = read & overwrite at start
x = create new file 
a = append (add at the end)
b = binary
t = text
+ = read and write

Keep checking the zzz.txt file to see the changes

'''
#Writing a file

f = open("zzz.txt", "w")
f.write("I'm a student")
f.write("\nI love programming")
f.close

print()
# Read line

f = open("zzz.txt", "r")
data = f.readline()
print(data)
f.close

print()
# Reading a file

f = open("zzz.txt", "r")
data = f.read()
print(data)
f.close

print()
# Append a file

f = open("zzz.txt", "a")
f.write("\nI'm from Dhaka")
f.close
