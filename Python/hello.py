# Ask user for their name
from os import sep


name = input("What's your name? ").strip().capitalize().title()

# Say hello to user
print("Hello,", name, end=" ")
# This is a format string
print(f"Bye, {name}")
