x=input()
a,b,c,d=0,0,0,0
s="aeiouAEIOU"
m="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for char in x:
    if char.isdigit():
        c+=1
    if char in s:
        a+=1
    if char==' ':
        d+=1
    if char in m:
        b+=1
print('Vowels: %d'%a)
print('Consonants: %d'%b)
print("Digits: %d"%c)
print("White spaces: %d"%d)