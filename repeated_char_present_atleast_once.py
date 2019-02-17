# atleast once
a,b=map(str,input().split())
c=0
for i in range(len(a)):
	if a[i]==b[i]:
		c=c+1
if c>0:
	print("yes")
else:
	print("no")
