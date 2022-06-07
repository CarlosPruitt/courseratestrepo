# Set up an infinte loop
while True:
# Gets input from keyboard
	line = input()	
# If input is 'done', 'd', or 'Done', break out of the infinite loop
	if line == 'done' or line == 'd' or line == 'Done':
		break
# Print the input from the user in reverse order
	print(line[::-1])

