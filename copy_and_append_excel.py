import pandas as pd
from pathlib import Path
from openpyxl import load_workbook
def write_wave_exchange():
    """Reader wave exchange excel file.

    Args:
        file_path (str | Path): path to Wave Exchange Excel File.
   
    Returns:
        wave_exchange: wave exchange table as DataFrame.
    """
    data_folder = Path(r'.')
    input_file = data_folder / 'test_02.xlsx'
    output_file_path =  data_folder / (
        input_file.stem + '_out' + input_file.suffix)

    print('Write to output file.')
    
    writer = pd.ExcelWriter(output_file_path, engine='openpyxl')
    
    writer.book = load_workbook(filename = input_file)
    writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
    sheet = 'Sheet1'
    df_data = pd.DataFrame(writer.book[sheet].values)
    df_data.columns = list(df_data.iloc[0])
    df_data = df_data.iloc[1:, :]
    df_data['FILE_NAME'] ='new_name'
    df_data['DLC_DESCR'] ='new_descr'
    
    df_data.to_excel(writer, sheet_name=sheet, columns=['FILE_NAME'],
                     startrow=1, header=0, startcol=2, index=False)
    df_data.to_excel(writer, sheet_name=sheet, columns=['DLC_DESCR'],
                     startrow=1, header=0, startcol=4, index=False)

    writer.save()
    
