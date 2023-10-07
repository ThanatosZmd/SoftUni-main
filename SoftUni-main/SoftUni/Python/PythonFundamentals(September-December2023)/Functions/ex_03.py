def range_chars(a: str, b: str):
    chars = []
    for i in range(ord(a)+1, ord(b)):
        chars.append(chr(i))
    return chars

first_char = input()
second_char = input()
print(*range_chars(first_char,second_char), sep=" ")