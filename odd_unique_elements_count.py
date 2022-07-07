def unique(list1):
    unique_list = []
    s=0
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for z in unique_list:
        if z%2!=0:
            s+=1
    return s
n=int(input())
l=list(map(int,input().split()))
print(unique(l))