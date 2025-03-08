# .xls 使用xlrd读取，xlwt创建修改
# .xlsx openpyxl.readthedocs.io
import openpyxl as xl
book = xl.load_workbook("test.xlsx")
sheet = book.worksheets[0]
print(sheet.title)




