def reverse_string(word):
    if word == "":
        return ""

    return reverse_string(word[1:]) + word[0]


word = input()
result = reverse_string(word)
print(result)
