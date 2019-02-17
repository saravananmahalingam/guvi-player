# count of char repeats
a,b=map(str,input().split())
c=0
for i in range(len(a)):
	if a[i]==b[0]:
		c=c+1
print(c)
