import enchant

def is_real_words(paragraph):
    dictionary = enchant.Dict("en_US")
    words = paragraph.split()
    for word in words:
        if not dictionary.check(word):
            return False
    return True

print(is_real_words("this is a real sentence")) # True
print(is_real_words("this is not a real sentece")) # False

