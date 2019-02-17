# max divisible by both a and b
a,b=map(int,input().split())
li=[]
for i in range(1,b+1):
	if a%i==0 and b%i==0:
		li.append(i)
print(max(li))
