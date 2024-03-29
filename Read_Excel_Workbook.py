#Open an Excel workbook:

    import xlrd
    workbook = xlrd.open_workbook('my_workbook.xls')

#Grab list of worksheets in a workbook:

    import xlrd
    workbook = xlrd.open_workbook('my_workbook.xls')
    print workbook.sheet_names()

#Grab a specific worksheet from a workbook:

    import xlrd
    workbook = xlrd.open_workbook('my_workbook.xls')
    worksheet = workbook.sheet_by_name('Sheet1')

#Iterate over each worksheet in a workbook:

    import xlrd
    workbook = xlrd.open_workbook('my_workbook.xls')
    worksheets = workbook.sheet_names()
    for worksheet_name in worksheets:
    	worksheet = workbook.sheet_by_name(worksheet_name)
    	print worksheet

#Iterate over each row of a worksheet:

    import xlrd
    workbook = xlrd.open_workbook('my_workbook.xls')
    worksheet = workbook.sheet_by_name('Sheet1')
    num_rows = worksheet.nrows - 1
    curr_row = -1
    while curr_row < num_rows:
    	curr_row += 1
    	row = worksheet.row(curr_row)
    	print row

#Grab the cell contents of each row of a worksheet:

    import xlrd
    workbook = xlrd.open_workbook('my_workbook.xls')
    worksheet = workbook.sheet_by_name('Sheet1')
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = -1
    while curr_row < num_rows:
    	curr_row += 1
    	row = worksheet.row(curr_row)
    	print 'Row:', curr_row
    	curr_cell = -1
    	while curr_cell < num_cells:
    		curr_cell += 1
    		# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
    		cell_type = worksheet.cell_type(curr_row, curr_cell)
    		cell_value = worksheet.cell_value(curr_row, curr_cell)
    		print '	', cell_type, ':', cell_value
