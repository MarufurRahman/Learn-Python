

#recursive function
def counter(a):
	print(a)
	a = a+1
	counter(a)
counter(1)