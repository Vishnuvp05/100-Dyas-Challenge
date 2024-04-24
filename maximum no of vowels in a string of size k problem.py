#maximum no of vowels in a string of size k problem 


s="bacacbefaobeacfe"
k=5
a="aeiou"
maxvowel=0
for i in s[:k]:
    if i in a:
        maxvowel+=1
total=maxvowel
for i in range(len(s)-k):
    if s[i] in a:
        total-=1
    if s[i+k] in a:
        total+=1
    maxvowel=max(maxvowel,total)

print(maxvowel)





