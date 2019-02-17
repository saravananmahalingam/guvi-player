# count the given string is repeats in a list
a=list(map(str,input().split()))
b=input()
c=0
for i in range(len(a)):
	if a[i]==b:
		c=c+1
print(c)
