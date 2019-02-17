# 1st address
a,b=map(str,input().split())
for i in range(len(a)):
	if a[i]==b[0]:
		print(i+1)
		break;
