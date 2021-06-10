# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("sample.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(5, 4))

Dict = {'G': '1st Floor', 'T': 'Top', 'F': 'Furnished','P': 'Pool View'}
#print(Dict)

Codes = ['GF', 'PFT']

# Iterate over list of codes
for i in range(0,len(Codes)):
    code_len = len(Codes[i])
    #print("here")
    Description = ""
    # Iterate over code
    for j in Codes[i]:
        #print(j)
        #print(Dict[j])
        Description =  Description + ", " + Dict[j]
    Description = Description[2:]
    print(Description)
