# Problem 1 lab 1

VOWELS ="aeiou"  # I write it in UPPER CASE this is a notation for constants


def vowels_number(word):
    global VOWELS #to define a global variable
    count=0
    for c in word:
        if c in VOWELS:
            count+=1
    return count


word_=input("Enter A Word: ") # Type: String
print(f"The Number of Vowels = {vowels_number(word_)}") 