
import random
import string

length = int(input("Password length (min 8): "))
while length < 8:
    length = int(input("Min 8! Enter again: "))

chars = ""
if input("Lowercase? (y/n): ").lower() == "y":
    chars += string.ascii_lowercase
if input("Uppercase? (y/n): ").lower() == "y":
    chars += string.ascii_uppercase
if input("Numbers? (y/n): ").lower() == "y":
    chars += string.digits
if input("Symbols? (y/n): ").lower() == "y":
    chars += string.punctuation

if chars:
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Password:", password)
else:
    print("Select at least one type!")
