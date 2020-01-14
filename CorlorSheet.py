# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:52:45 2020

@author: JLi
"""
import os,time
import pandas as pd
import numpy as np


Colors=['#f7cac9','#f5ed82','#f7e1c3','#f0f2c9','#affacd','#a5f090','#97f4f7',
        '#adc9ff','#9f9ffc','#dbc1f7','#f3befa','#f2acd0','#f2221b','#f2eb1b',
        '#f7f011','#46ed0e','#0ec0ed','#0e42ed','#aa0eed','#d70eed','#ed0ecc']


                        	
import os,time
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

Colors=['#f7cac9','#f5ed82','#f7e1c3','#f0f2c9','#affacd','#a5f090','#97f4f7',
        '#adc9ff','#9f9ffc','#dbc1f7','#f3befa','#f2acd0','#f2221b','#f2eb1b',
        '#f7f011','#46ed0e','#0ec0ed','#0e42ed','#aa0eed','#d70eed','#ed0ecc']

Colors=np.array(Colors)
df=pd.DataFrame(Colors.reshape([7,3]))
savefilename='CorlorSheet.xlsx'
def excel_wrap_save(df,savefilename,sheetname='Sheet1'):
    #savefilename=os.path.join(savePath,'result_all.xlsx')
       
    writer = pd.ExcelWriter(savefilename, engine='xlsxwriter')
    df.to_excel(writer,sheet_name=sheetname, startrow=1, header=False,index=False)
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    
    # Add a header format.
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#fff8b6',
        'border': 1})
    
    for ind_num, ind_value in  enumerate(df.index.values):
        for col_num, col_value in enumerate(df.columns.values): 
            format1 = workbook.add_format({ 
                    'fg_color': df.loc[ind_value,col_value], 'border': 1})           
            worksheet.write(ind_num+1,col_num,df.loc[ind_value,col_value],format1)
            
                    
            
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
      
