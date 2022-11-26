from csv import excel
import pandas as pd 


excel_data = pd.read_excel(
                            "mashina.xlsx",
                            sheet_name = "Sheetl",
                            usecols =["Название","Цена","Доп.инфа"]                            
                            )


print(excel_data)


import xlrd  

filic = xlrd.open_workbook_xls("mashina.xls",formatting_info=True)
sheet = filic.sheet_by_index(0)
column = sheet.col_values(0,1) 
print(column) 





