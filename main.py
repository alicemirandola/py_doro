import pandas as pd

def main():

    xls = pd.ExcelFile("sample_spreadsheet.xlsx")

    sheetX = xls.parse(0) #2 is the sheet number

    var1 = sheetX['Year']

    print(var1[2]) #1 is the row number...

main()
