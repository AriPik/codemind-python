s=input()
v=list("aeiou")
for i in s:
    if i in v:
        v.remove(i)
if(len(v)==0):
    print("True")
else:
    print("False")