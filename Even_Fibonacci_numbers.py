fib=[1, 2]
ev=[]

def next_fib(pred, last):
	fib.append((pred+last))
while fib[-1]<4000000:
	x=fib[-1]
	z=fib[-2]
	next_fib(z,x)

if z+x>4000000:
	fib.pop()

for num in fib:
	if num%2==0:
		ev.append(num)

print(fib)
print(sum(ev))