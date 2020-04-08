from DIP import DIP_create
from SO import SO_create

print('KiCad Footprint Generation Tool')
print('Enter FP type:')
series = input()

if series == 'DIP':
	DIP_create(28)
elif series == 'SO':
	SO_create(28, 'W')
	SO_create(28, 'X')
else:
	print('No matches')
