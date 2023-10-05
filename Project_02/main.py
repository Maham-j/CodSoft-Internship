import random

# Define the character sets
# List of letters
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

# List of symbols
symbols = ['#', '!', '$', '%', '&', '*', '+', ',','^','@']

# Welcome message and input from the user
print('Welcome to the PyPassword Generator')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_numbers = int(input('How many numbers would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like in your password?\n'))

# Initialize an empty list to hold password characters
pass_chr = []

# Generate requested number of letters
for letter in range (nr_letters):
    pass_chr.append(random.choice(letters))

# Generate requested number of numbers    
for number in range (nr_numbers):
    pass_chr.append(random.choice(numbers))

# Generate requested number of symbols    
for symbol in range (nr_symbols):
    pass_chr.append(random.choice(symbols))

# Shuffle the characters for randomness
random.shuffle(pass_chr)
 
# Construct the final password by joining characters   
password = ''
for pas in pass_chr:
    password += pas

# Display the generated password 
print(f'Your required password is:{password}')
    
