# Using the superhero and supervillain packages to generate names
import heroes as h
import villains as v

emp = []

# Printing an array of names
print(h.genarr(10))
print(v.genarr(3))

# Storing it in an array
h1 = h.genarr(10)

# with open("h.txt", mode="a") as f:
# 	f.write(str(h1))

# Open the file in write mode
with open("h.txt", mode="w") as f:
	# Iterate through the array and write each name to the file on a new line
	for name in h1:
		f.write(name + "\n")
