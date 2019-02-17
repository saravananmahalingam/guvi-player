# start from 2 number
a=int(input())
b=list(map(int,input().split()))
b.sort()
print(*b[1:])
