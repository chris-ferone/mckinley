# Reading an excel file using Python
import pandas as pd
import math
df = pd.read_excel(r'C:\Repos\mckinley\Unit Type v3.2.xlsx', header=5, sheet_name='AC', usecols="A,AC:AD", nrows=100)
#print("start")
#print(df)
#print("end")
#print(df.iloc[9:54, 1:3])
#print(pd.Series(df.iloc[9:19, 2],index=df.iloc[9:19, 3]).to_dict())
#print(xcl_dict)
#AC16
#dict =
#print("column names")
#print(df.columns.values)
#['Type' 'Unnamed: 28' 'Count.1']
#print(df['Unnamed: 28'])

codes = df.iloc[:, 0].tolist()
clean_codes=[]
for i in codes:
    if str(i) == 'nan':
        break
    else:
        clean_codes.append(i)
#print(codes)
print("codes")
print(clean_codes)
print("")
dict_keys = df.iloc[9:54, 1].tolist()
dict_values = df.iloc[9:54, 2].tolist()
dict={}
for i in range(len(dict_keys)):
    if type(dict_keys[i]) != str:
        break
    else:
        dict[dict_keys[i]] = dict_values[i]
print("Dictionary")
print(dict)
# dict = {'G': '1st Floor', 'T': 'Top', 'F': 'Furnished','P': 'Pool View'}
# #print(dict)
#
# codes = ['GF', 'PFT']
#
# Iterate over list of codes
for i in range(0,len(clean_codes)):
    code_len = len(clean_codes[i])
    #print("here")
    Description = ""
    # Iterate over code
    #print(codes[i])
    first_run = True
    for j in clean_codes[i]:
        #print(j)
        if not first_run:
            Description =  Description + ", " + dict[j]
        else:
            first_run = False
    Description = Description[2:]
    print(Description)
