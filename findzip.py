import openpyxl
import sys


doc = openpyxl.load_workbook('RecycleLocations.xlsx')
sheet = doc.get_sheet_by_name('RecycleLocations')

user_input = str(sys.argv[1])

i = 2
while i != 100:
	Avalue = 'A' + str(i)
	Bvalue = 'B' + str(i)
	Cvalue = 'C' + str(i)
	if sheet[Bvalue].value == user_input:
		print(sheet[Avalue].value + " at " + sheet[Cvalue].value)

	i = i + 1
