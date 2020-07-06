def composite(s):
	list_a= []
	for i in range(2, s + 1):
		for j in range(2, i):
			if i % j == 0 :
				list_a.append(i)
				break
	return list_a
def primer(se):
	primes = [2, 3, 5, 7]
	r = primes[:]
	for a in range(8, int(se) + 1):
		if any(a % k == 0 for k in primes):
			print(a)
			continue
		r.append(a)
	return r
