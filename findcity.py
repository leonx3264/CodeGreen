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
	Dvalue = 'D' + str(i)
	if sheet[Dvalue].value == user_input or sheet[Bvalue].value == user_input:
		print("<li><h3>" + sheet[Avalue].value + "</h3><p>" + sheet[Cvalue].value + "</p></li>")

	i = i + 1

