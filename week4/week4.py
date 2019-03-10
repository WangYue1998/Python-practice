# Poorly documented program with poorly chosen variable names
# so as to remain a "mystery"


w = input("Enter anything: ")

#e = len(w) - 1
#s = 0
r=''

for c in w:
    if 'a'<= c.lower()<= "z":
        r += c
    e = len(r) - 1
    s = 0
        
while s < e:
    if r[e].lower() == r[s].lower():
        s = s + 1
        e = e - 1
    else:
        break
if 0 <= s < len(r) and 0 <= e < len(r) and  r[e] != r[s]:
        print ("Sorry, try again.")
else:
    print ("Bingo!")
     