import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@','#','$','%','^','&','*','(',')','+']

nr_letter = int(input('Enter how many letter do you want:\n'))
nr_number = int(input('Enter hoe many number do you want:\n'))
nr_symbol = int(input('Enter how many symbol do you want:\n'))

#----------------------------------------------------------------------------------------------------

# EASY WAY TO GENERATE

password = ""

for char in range(1, nr_letter + 1):
    password += random.choice(letter)
for char in range(1, nr_number + 1):
    password += random.choice(number)
for char in range(1, nr_symbol + 1):
    password += random.choice(symbol)

print(password)


#--------------------------------------------------------------------------------------------

#HARD WAY TO GENERATE

password_list = []

for char in range(1, nr_letter + 1):
    password_list += random.choice(letter)
for char in range(1, nr_number + 1):
    password_list += random.choice(number)
for char in range(1, nr_symbol + 1):
    password_list += random.choice(symbol)

print(password_list)

random.shuffle(password_list)

password = ""
for char in password_list: 
   password += char

print(f"Your password is : {password}")


