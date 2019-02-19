# square the digit and sum it
a=int(input())
c=0
while a:
	b=a%10
	c=c+(b**2)
	a=a//10
print(c)
