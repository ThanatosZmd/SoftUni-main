data = input()
new_data = ""
last_char = ""
for char in data:
    if char != last_char:
        new_data += char
        last_char = char
print(new_data)