
string = "ABC for the purpose of LetterCounting program"
print(string)
words = 1
letters = 0
hash_table = {}

for char in string:
    char = char.lower()
    if char  == ' ':
        words+=1
    else:
        letters+=1
        if char in hash_table:
            hash_table[char]+=1
        else:
            hash_table[char]=1
            

print("Words:", words, "Letters:", letters, "Freq:", hash_table)

