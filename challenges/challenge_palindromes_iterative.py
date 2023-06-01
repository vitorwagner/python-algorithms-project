def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    return word == word[::-1]
# https://www.w3schools.com/python/python_howto_reverse_string.asp
