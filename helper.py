import xlsxwriter
from parce_maps import array

def writer(parametr):
    book=xlsxwriter.Workbook(r'D:\pycharm_repository\pycharm_maps\.venv\parser_spark-interfax.xlsx')
    page = book.add_worksheet('data')

    row = 0
    column = 0

    page.set_column('A:A',20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)
    page.set_column('E:E', 50)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        row +=1
        print('добавлена кампания',row)
    book.close()

writer(array)