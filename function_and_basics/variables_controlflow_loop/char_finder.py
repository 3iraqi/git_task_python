# Problem 2 lab 1

def check_char():
    ...
def char_index(word,char):
    locations=[]
    if char not in word:
        return(f"{char} not Found!")
    for i in range(len(word)):
        if word[i] == c:
            locations.append(i)
    del locations        
    return(f"The {char} char Founded in these locations : {locations} ")


print("Char index Finder:\n")

word_=input("Enter The Word:  ")
c = input('Enter The Char:  ')
print(char_index(word_,c))