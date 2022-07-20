s=input()
a=s.split()
l=len(a)
k=a[l-1]
w=min(k)
if w>='A' and w<='Z' or w>='a' and w<='z':
    if w.lower() in k:
        print(w.lower())
    else:
        print(w)