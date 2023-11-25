def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x
def decipher_message(secret_message):
    deciphered_words = []
    words = secret_message.split()
    digits = []

    for word in words:
        word = list(word)
        word = [try_int(x) for x in word]
        for el in word:
            if el is int:
                digits.append(el)
                word.remove(el)
        digit = sum(digits)
        word.insert(0, chr(digit))
        word[1], word[len(word)-1] = word[len(word)-1], word[1]
        deciphered_words.append("".join(word))


    # Join the deciphered words to form the complete message
    deciphered_message = ' '.join(deciphered_words)
    return deciphered_message


# Example usage
secret_message = input()
deciphered_message = decipher_message(secret_message)
print("Deciphered message:", deciphered_message)
