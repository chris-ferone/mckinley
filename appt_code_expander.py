# Reading an excel file using Python
import pandas as pd
import math

# Read in data from Excel Spreadsheet. Starting at row 5(zero-indexed), read in
# the next 100 rows, but only read in column A, AC, and AD.
df = pd.read_excel(r'C:\Repos\mckinley\Unit Type v3.2.xlsx', header=5, sheet_name='AC', usecols="A,AC:AD", nrows=100)

# Extract the appartment codes from column A into a list
codes = df.iloc[:, 0].tolist()

# Remove the "nan" codes from the apartment codes list
clean_codes=[]
for i in codes:
    if str(i) == 'nan':
        break
    else:
        clean_codes.append(i)

# Create a dictionary of key-value pairs from columns AC and AD
dict_keys = df.iloc[9:54, 1].tolist()
dict_values = df.iloc[9:54, 2].tolist()
dict={}
for i in range(len(dict_keys)):
    if type(dict_keys[i]) != str:
        break
    else:
        dict[dict_keys[i]] = dict_values[i]
#print("Dictionary")

# Iterate over list of codes, generate string from each code using dictionary
for i in range(0,len(clean_codes)):
    code_len = len(clean_codes[i])
    Description = ""
    # Iterate over code
    first_run = True
    for j in clean_codes[i]:
        if not first_run:
            Description =  Description + ", " + dict[j]
        else:
            first_run = False
    Description = Description[2:]
    print(Description)
