# writing to the file

# Opening a file
# with open("my.txt") as file:
# 	contents = file.read()
# 	print(contents)

# Note appending and then going back to position 1 and then reading file

# with open("my.txt", mode="a+") as f:
# 	f.write("Suck and fuck")
# 	f.seek(0)
# 	contents = f.read()
# 	print(contents)

with open("my.txt", mode="a") as f:
	f.write("\nsuck")