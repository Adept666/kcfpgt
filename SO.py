def head(f, n, w = ''):
	#! There is no suffix processing yet
	timestamp = '00000000'	#!
	ref_y = 0	#!
	val_y = 0	#!
	f.write('(module P-SO-%02d (layer F.Cu) (tedit %s)\n' % (n, timestamp))
	f.write('  (fp_text reference REF** (at 0 %.3f) (layer F.SilkS)\n' % ref_y)
	f.write('    (effects (font (size 1 1) (thickness 0.2)))\n')
	f.write('  )\n')
	f.write('  (fp_text value P-SO-%02d (at 0 %.3f) (layer F.Fab)\n' % (n, val_y))
	f.write('    (effects (font (size 1 1) (thickness 0.2)))\n')
	f.write('  )\n')
	return 0

def F_SilkS(f, n, w = ''):
	if w == '':
		a = 8.89
	elif w == 'A':
		a = 8.89
	elif w == 'W':
		a = 12.7
	elif w == 'X':
		a = 13.97
	e = 1.27
	b = e * (0.5 * n + 1)
	yt = str(-b / 2)
	yb = str(b / 2)
	xl = str(-a / 2)
	xr = str(a / 2)
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.SilkS) (width 0.2))\n' % (xl, yt, xr, yt))
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.SilkS) (width 0.2))\n' % (xl, yb, xr, yb))
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.SilkS) (width 0.2))\n' % (xl, yt, xl, yb))
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.SilkS) (width 0.2))\n' % (xr, yt, xr, yb))
	return 0

def F_Fab(f, n, w = ''):
	if w == '':
		a = 3.90
	elif w == 'A':
		a = 5.29
	elif w == 'W':
		a = 7.50
	elif w == 'X':
		a = 8.89
	#
	if (n == 8) and (w == ''):
		b = 4.9
	elif (n == 8) and (w == 'A'):
		b = 5.24
	elif (n == 8) and (w == 'W'):
		b = 5.25
	#
	elif (n == 14) and (w == ''):
		b = 8.65
	elif (n == 14) and (w == 'W'):
		b = 9
	#
	elif (n == 16) and (w == ''):
		b = 9.9
	elif (n == 16) and (w == 'W'):
		b = 10.3
	#
	elif (n == 20) and (w == 'W'):
		b = 12.8
	#
	elif (n == 24) and (w == 'W'):
		b = 15.695
	elif (n == 24) and (w == 'X'):
		b = 15.695
	#
	elif (n == 28) and (w == 'W'):
		b = 18.235
	elif (n == 28) and (w == 'X'):
		b = 18.235
	#
	elif (n == 32) and (w == 'W'):
		b = 20.775
	elif (n == 32) and (w == 'X'):
		b = 20.775
	#
	elif (n == 36) and (w == 'W'):
		b = 23.315
	elif (n == 36) and (w == 'X'):
		b = 23.315
	#
	yt = str(-b / 2)
	yb = str(b / 2)
	xl = str(-a / 2)
	xr = str(a / 2)
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.Fab) (width 0.2))\n' % (xl, yt, xr, yt))
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.Fab) (width 0.2))\n' % (xl, yb, xr, yb))
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.Fab) (width 0.2))\n' % (xl, yt, xl, yb))
	f.write('  (fp_line (start %s %s) (end %s %s) (layer F.Fab) (width 0.2))\n' % (xr, yt, xr, yb))
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
