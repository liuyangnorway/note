from openpyxl import load_workbook
# Open a temp excel
workbook = load_workbook(filename =temp_excel_file)
# add new data
# workbook
# save to a new excel file
workbook.save(filename = new_excel_file)
