import string
import random
import enchant
import sys

# Create enchant dictionary object
d = enchant.Dict("en_US")

def is_real_words(paragraph):
    """
    Check if at least 5 words out of randomly selected words are real words.
    """
    words = paragraph.split()
    # Randomly select 7 words from the list of words
    random_words = random.choices(words, k=7)
    real_word_count = 0
    for word in random_words:
        if d.check(word):
            real_word_count += 1
    # Return True if at least 5 words are real words
    return real_word_count >= 4


def decipher_caesar(ciphertext, shift):
    """
    Decrypts the ciphertext using a Caesar Cipher with the given shift value.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - shift - 65) % 26 + 65)
                plaintext += shifted_char
            else:
                shifted_char = chr((ord(char) - shift - 97) % 26 + 97)
                plaintext += shifted_char
        else:
            plaintext += char
    return plaintext


# Open the file specified in the first command line argument
f = open(sys.argv[1], "r").read()
result = "Result not found"

# Try all possible shift values
for shift_value in range(26):
    decry = decipher_caesar(f, shift_value)
    if is_real_words(decry):
        result = decry
        break
print(result)
