letters=['a','b','c','d','e','i','j','o']
def filter_vowels(letter):
    vowels=['a','e','i','o','u']
    return True if letter in vowels else False

filtered_vowels=filter(filter_vowels,letters)
print(tuple(filtered_vowels))
