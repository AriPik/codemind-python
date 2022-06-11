l=int(input())
n=int(input())
while n:
    w,h=map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w>=l and h>=l:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")
    n=n-1