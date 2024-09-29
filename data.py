import pandas as pd

file_path = '/mnt/data/dataKasus-1.xlsx'
excel_data = pd.ExcelFile(file_path)

sheet_names = excel_data.sheet_names
sheet_names


df = pd.read_excel(file_path, sheet_name='2022')

df.head()

df.columns = ['No', 'Nama', 'Usia', 'Paritas', 'Jarak_Kelahiran', 'Riw_Hipertensi', 
              'Riw_PE', 'Obesitas', 'Riw_DM', 'Riw_Hipertensi_PE_Keluarga', 
              'Sosek_Rendah', 'PE_NonPE', 'Unused']

df_cleaned = df.drop(columns=['Nama', 'Unused'])

df_cleaned['Usia'] = df_cleaned['Usia'].str.replace(' TH', '').astype(int)

df_cleaned.head()
