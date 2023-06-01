def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if word[low_index] != word[high_index]:
        return False
    if high_index - low_index <= 1:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
