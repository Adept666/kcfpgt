def head(f, n, w = ''):
	return 0

def F_SilkS(f, n, w = ''):
	return 0

def F_Fab(f, n, w = ''):
	return 0

def F_CrtYd(f, n, w = ''):
	return 0

def pads(f, n, w = ''):
	if w == '':
		c = 5.20
	elif w == 'A':
		c = 6.10
	elif w == 'W':
		c = 9.20
	elif w == 'X':
		c = 10.80
	e = 1.27
	for i in range(1, n + 1):
		if i <= n / 2:
			x = -(c / 2)
			y = -e * (0.25 * n + 0.5 - i)
		else:
			x = c / 2
			y = e * (0.75 * n + 0.5 - i)
		line = '  (pad ' + str(i) + ' smd rect (at ' + str(x) + ' ' + str(y) + ') (size 2.2 0.6) (layers F.Cu F.Mask))\n'
		f.write(line)
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
