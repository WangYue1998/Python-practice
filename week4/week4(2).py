w = input("Enter a title: ")
import string
r=''
for c in w:
    
    if c not in string.punctuation and string. whitespace:
        r+=c
        print(r)
    
