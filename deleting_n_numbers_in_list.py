# print aafter deleting b
a,b=map(int,input().split())
c=list(map(int,input().split()))
print(*c[0:-b])
