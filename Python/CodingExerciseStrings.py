import random
word=(input("Please input a string."))
n=0
y=1
z=0
w=""
x=""
jumble=""
for c in word:
    n+=1
z=n+0
while y<=n:
    z-=1
    w+=word[z]
    y+=1
print(w)
while w:
    position=random.randrange(len(w))
    jumble+= w[position]
    w= w[:position]+w[(position+1):]
print(jumble)