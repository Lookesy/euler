nums=list(range(1, 1000))

def mul(nums):
	approve=[]
	for num in nums:
		if num%3==0 or num%5==0:
			approve.append(num)

	print(sum(approve))


mul(nums)
