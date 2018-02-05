def average(lst):
	d=len(lst)
	s=0
	for x in lst:
		s += x
	y= round(s/d, 3)
	return (y)