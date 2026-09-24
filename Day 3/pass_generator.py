import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

num_letters = 6
num_numbers = 2
num_symbols = 2

password_list = []

for _ in range(num_letters):
    password_list.append(random.choice(letters))
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = "".join(password_list)

print(f"Generated Password: {password}")