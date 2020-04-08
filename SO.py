def head(f, n, w = ''):
	return 0

def F_SilkS(f, n, w = ''):
	return 0

def F_Fab(f, n, w = ''):
	return 0

def F_CrtYd(f, n, w = ''):
	return 0

def pads(f, n, w = ''):
	return 0

def SO_create(n, w = ''):
	f = open('P-SO-28W.kicad_mod', 'w')
	#f = open('P-SO-28X.kicad_mod', 'w')
	head(f, n, w)
	F_SilkS(f, n, w)
	F_Fab(f, n, w)
	F_CrtYd(f, n, w)
	pads(f, n, w)
	f.write(')')
	f.close()
	return 0
