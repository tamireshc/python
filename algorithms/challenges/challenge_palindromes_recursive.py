def is_palindrome_recursive(word, low_index, high_index):
    if word is None or word == "":
        return False
    elif len(word) == 1 or len(word) == 0:
        return True
    elif word[-1] == word[0] and len(word) == 2:
        return True
    elif word[-1] == word[0]:
        return is_palindrome_recursive(word[1:-1], 0, len(word) - 1)
    else:
        return False


# print(is_palindrome_recursive("GG", 0, len("GG") - 1))
# print(is_palindrome_recursive("SOCOS", 0, len("SOCOS") - 1))
# print(is_palindrome_recursive("REVIVER", 0, len("REVIVER") - 1))
# print(is_palindrome_recursive("COXINHA", 0, len("COXINHA") - 1))
# print(is_palindrome_recursive("AGUA", 0, len("AGUA") - 1))
