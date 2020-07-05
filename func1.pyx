def composite(s):
	list_a=[]
	for i in range(2,s+1):
		for j in range(2,i):
			if i % j == 0 :
				list_a.append(i)
				break
	return list_a
def primer(se):
	i=se
	r=list()
	r.append(2)
	r.append(3)
	r.append(5)
	r.append(7)
	for a in range(8,int(i)+1):
		if a%2 == 0 or a%3 == 0 or a%5 == 0 or a%7 == 0 :
			print(a)
			continue
		else:
			r.append(a)
	return r
