ascii_string = ""
with open('dictionary.txt', 'r') as file:
    for line in file:
        integer = int(line.strip())
        character = chr(integer)
        ascii_string += character

print("ASCII string:", ascii_string)

