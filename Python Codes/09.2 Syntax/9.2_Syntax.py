''' Keep checking the ccc.txt file for the changes '''

# Reading from file
with open("ccc.txt", "r") as f:
    data = f.read()
    print("File content:", data)

print( )
# Appending to file
with open("ccc.txt", "a") as f:
    f.write("\nI'm a student")  # Added newline and removed data2
    print(data)
