from numvalid import is_valid
		
def main():
	ldata =[
		["9553015305",True],
		["9985489620",True],
		["abced43565",False],
		["a1234b2346",False],
		["9885983136",True],
		["999 324 1234",False],
		["0091 8792098020",True],
		["+91 9652844138",True],
		["737-423-4734",True]
		]
	for d in ldata:
		rvalue = is_valid(d[0])
		if(rvalue != d[1]):
			print(d[0],"fail")
		else:
			print(d[0],"pass")
	
if(__name__=="__main__"):
	main()

