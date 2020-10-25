# your code goes here
t = int(input())
pp = 1
while t>0:	
	n = int(input())
	s = input()
	
	a,b = 0,0
	for i in s:
		if i == 'A': a+=1
		else: b+=1
	
	print ('Case #'+str(pp)+': ', end = ' ')
	pp+=1
	if abs(a-b) == 1: print ('Y')
	else: print ('N')
	t-=1
