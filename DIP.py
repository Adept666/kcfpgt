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
	return 0

def F_Fab(f, n, w = ''):
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
