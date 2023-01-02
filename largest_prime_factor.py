znum=600851475143
lli=[]
prov=znum/2
round(prov, 0)
prov=int(prov)
x=True
xnum=prov

while x==True:
	if znum%xnum==0:
		k=0
		for i in range(2, xnum // 2+1):
			if (xnum % i == 0):
				k = k+1
		if k <= 0 and xnum!=1:
			lli.append(xnum)
			x=False
		
	xnum=xnum-1

print(lli[-1])