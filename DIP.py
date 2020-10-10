def head(f, n, w = ''):
	#! There is no suffix processing yet
	timestamp = '00000000'	#!
	ref_y = 0	#!
	val_y = 0	#!
	f.write('(module P-DIP-%02d (layer F.Cu) (tedit %s)\n' % (n, timestamp))
	f.write('  (fp_text reference REF** (at 0 %.3f) (layer F.SilkS)\n' % ref_y)
	f.write('    (effects (font (size 1 1) (thickness 0.2)))\n')
	f.write('  )\n')
	f.write('  (fp_text value P-DIP-%02d (at 0 %.3f) (layer F.Fab) hide\n' % (n, val_y))
	f.write('    (effects (font (size 1 1) (thickness 0.2)))\n')
	f.write('  )\n')
	return 0

def F_SilkS(f, n, w = ''):
	if w == '':
		a = 10.16
	elif w == 'L':
		a = 12.7
	elif w == 'X':
		a = 17.78
	e = 2.54
	b = e * (0.5 * n)
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
		a = 6.605
	elif w == 'L':
		a = 9.02
	elif w == 'X':
		a = 13.525
	#
	if (n == 8) and (w == ''):
		b = 9.88
	#
	elif (n == 14) and (w == ''):
		b = 19.305
	#
	elif (n == 16) and (w == ''):
		b = 20.13
	#
	elif (n == 18) and (w == ''):
		b = 22.48
	#
	elif (n == 20) and (w == ''):
		b = 25.2
	#
	elif (n == 22) and (w == 'L'):
		b = 27.555
	#
	elif (n == 24) and (w == ''):
		b = 30.45
	elif (n == 24) and (w == 'L'):
		b = 30.095
	elif (n == 24) and (w == 'X'):
		b = 31
	#
	elif (n == 28) and (w == ''):
		b = 35.2
	elif (n == 28) and (w == 'X'):
		b = 37.4
	#
	elif (n == 40) and (w == 'X'):
		b = 51.75
	#
	elif (n == 48) and (w == 'X'):
		b = 61.9
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
		c = 7.62
	elif w == 'L':
		c = 10.16
	elif w == 'X':
		c = 15.24
	e = 2.54
	for i in range(1, n + 1):
		shape = 'circle' if i == 1 else 'rect'
		if i <= n / 2:
			x = -(c / 2)
			y = -e * (0.25 * n + 0.5 - i)
		else:
			x = c / 2
			y = e * (0.75 * n + 0.5 - i)
		line = '  (pad ' + str(i) + ' thru_hole ' + shape + ' (at ' + str(x) + ' ' + str(y) + ') (size 2 2) (drill 1) (layers *.Cu *.Mask))\n'
		f.write(line)
	return 0

def DIP_create(n, w = ''):
	f = open('P-DIP-28.kicad_mod', 'w')
	head(f, n, w)
	F_SilkS(f, n, w)
	F_Fab(f, n, w)
	F_CrtYd(f, n, w)
	pads(f, n, w)
	f.write(')')
	f.close()
	return 0
