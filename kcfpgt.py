print('KiCad Footprint Generation Tool')
print('Enter FP type:')
series = input()

if series == 'DIP':
	f = open('P-DIP-28.kicad_mod', 'w')
	f.write(')')
	f.close()
elif series == 'SO':
	f = open('P-SO-28W.kicad_mod', 'w')
	f.write(')')
	f.close()
	f = open('P-SO-28X.kicad_mod', 'w')
	f.write(')')
	f.close()
else:
	print('No matches')
