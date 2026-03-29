# Task1
inputs = []

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")

    if user_input.lower() == "stop":
        break

    inputs.append(user_input)

numbers = []

for x in inputs:
    try:
        numbers.append(int(float(x)))   # handles floats and integers
    except ValueError:
        pass

print("Numbers:", numbers)
print("Sum:", sum(numbers))
print("Smallest value:", min(numbers))


# Task2
text = "python is awesome!"
vowels = "aeiou"

new_string = ""
char_list = []

for char in text:
    if char == " ":
        transformed = "_"
    elif char.lower() in vowels:
        transformed = "#"
    else:
        transformed = char

    new_string += transformed
    char_list.append(transformed)

print("New string:", new_string)
print("Character list:", char_list)

# Task3
n = int(input("Enter a positive number: "))

countdown = []
current = n

while current > 0:
    countdown.append(current)
    current -= 1

print("List:", countdown)

joined = " -> ".join(map(str, countdown))
print("Joined:", joined)