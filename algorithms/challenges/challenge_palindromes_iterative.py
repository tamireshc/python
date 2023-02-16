def is_palindrome_iterative(word):
    reverse_word = ""
    if word is None or word == "":
        return False

    for index, letter in enumerate(word):
        if index == 0:
            pass
        else:
            reverse_word += word[-index]

    if word == reverse_word + word[0]:
        return True
    else:
        return False


# print(is_palindrome_iterative("COXINHA"))
# print(is_palindrome_iterative("SOCOS"))
# print(is_palindrome_iterative("GG"))

# AHNIXOC
