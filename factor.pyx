def factor(m):

	return [i for i in range(1, m + 1) if not m % i]

def dpf(number):

	i = (i for i in range(number) if len(factor(i)) == 2)
	u = []
	
	for num in i:
		while number % num == 0:
			number /= num
			u.append(num)
			
	return u
