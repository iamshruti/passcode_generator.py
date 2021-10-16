import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['!','@', '#', '$', '%', '&', '*', '(', ')', '+','=', '[', ']', '{', '}' ,'/' ,'?', '<', '>', ',', '.']

print("\n\n Welcome to the Python Passcode Generator!\n\n")
nr_letters = int(input("How many letters would you like in your passcode?\n")) 
nr_numbers = int(input(f"How many numbers would you like in your passcode?\n"))
nr_operators = int(input(f"How many operators would you like in your passcode?\n"))

passcode_list = []

for char in range(1, nr_letters + 1):
  passcode_list.append(random.choice(letters))

for char in range(1, nr_operators + 1):
  passcode_list += random.choice(operators)

for char in range(1, nr_numbers + 1):
  passcode_list += random.choice(numbers)

print(passcode_list)
random.shuffle(passcode_list)
print(passcode_list)

passcode= ""
for char in passcode_list:
  passcode += char

print(f"\nYour passcode is: {passcode}\n\n")
print("Thanks for using Python passcode Generator!❤️\n")