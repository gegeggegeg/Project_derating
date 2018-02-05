from read_BOM import *

reader = ReadBom('bom.csv')
sorted_data = reader.sort_component()
print(sorted_data.keys())
data = ''

while data != 'Q' :
	data = input('What data do yo want to see?\t')
	if data in sorted_data.keys():
		for res in sorted_data[data]:
			res.show_value()
	elif data == 'Q':
		print('Goodbye')
	else:
		print('Sorry, no such data')


