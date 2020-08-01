# Importing the built in library json file and importing the builtin to compare the similiar words
import json
from difflib import get_close_matches

# Loads the data json file
data = json.load(open('data.json'))
print("Welcome to the Interactive Dictionary")
# Function to return the definition of the word
def translate(w):
	# Check if the given word of the function call exists on the data file json
	# Turn the case insensitive
	w = w.lower()
	if w in data:
		return data[w]
	# Check If the word given in the first word upper case (Ex: Portugal, Paris, etc...)
	elif w.title() in data:
		return data[w.title()]
	elif w.upper() in data:
		return data[w.upper()]
	# Verify if the given word have similiarity than another words
	elif len(get_close_matches(w, data.keys())) > 0:
		# Asks if the user was meaning for the closest similiar given word
		ask_input = input(f'Did you mean {get_close_matches(w, data.keys())[0]} or {get_close_matches(w, data.keys())[1]} instead?\nPlease write Yes or No: ').lower()
		# If the user was wrote yes
		if ask_input == 'yes':
			# Turn the variable given word to the closest similiarity word
			# Asks if is the first or the second word
			ask1or2 = input(f'1. {get_close_matches(w, data.keys())[0]}\n2. {get_close_matches(w, data.keys())[1]}\nChoose an word by typing the number: ')
			# If is the first word
			if ask1or2 == '1':
				w = get_close_matches(w, data.keys())[0]
				# Show the definition of the given word
				return data[w]
			# If is the second word 
			elif ask1or2 == '2':
				w = get_close_matches(w, data.keys())[1]
				# Show the definition of the given word
				return data[w]
			else:
				return 'An error occured, please try again!'
			# Show the definition of the given word
			return data[w]
		# If the user wrote no
		elif ask_input == 'no':
			try:
				# Show the definition of the given word
				return data[w]
			# If there is no definition and doeśn't exists of the given word
			except:
				return "The word doesn't exists. Please double check it."
		# If the user did't typed well
		else:
			return "An error occured. Didn't understand the given input."
	else:
	# If not exists the word in data file json key.
		return "The word doesn't exists. Please double check it."

# Asks for the input of the user to return the definition
word = input("Enter a word: ")

# Run the function to return the definition of the given word in the input

# Turn the output in an variable to print out strings inside of the list
output = translate(word)

# Check if the output is an datatype as list
if type(output) == list:
	# Make an for to show all strings inside of the list
	for item in output:
		# Show all strings each one of the list
		print(item)
# If is not an list
else:
	# Show normal
	print(output)