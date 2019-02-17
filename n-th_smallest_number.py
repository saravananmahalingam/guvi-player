# n-th minimum
a,n=map(int,input().split())
b=list(map(int,input().split()))
b.sort()
print(b[n-1])
