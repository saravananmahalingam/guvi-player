# rotate right
a,b=map(int,input().split())
c=list(map(int,input().split()))
d=c[-b:]+c[:a-b]
print(*d)
