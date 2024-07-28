# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp..

# -- Work starting here

PLACE = "[name]"

with open("./Input/Names/invited_names.txt") as nf:
	names = nf.readlines()
	print(names)


with open("./Input/Letters/starting_letter.txt") as lf:
	lf = lf.read() # saved as string
	for n in names:
		s_n = n.strip()
		newL = lf.replace(PLACE, s_n)
		print(newL)
		with open(f"./Output/ReadyToSend/fuku_{s_n}.txt", mode="w") as ro:
			ro.write(newL)


