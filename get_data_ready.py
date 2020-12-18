import pandas as pd
import os
import zipfile

def get_data_ready(zipcode):
    naics = pd.read_csv(r'C:\Users\justi\Python Projects\PPP Analysis\PPP-Analysis\PPP Data\6-digit_2017_Codes.csv',encoding='latin1')
    naics = naics.drop('Unnamed: 2',axis=1)
    naics = naics[1:]
    naics.columns = ['NAICSCode', '2017 NAICS Title']

    arr = os.listdir(r"C:\Users\justi\Python Projects\PPP Analysis\PPP-Analysis\PPP Data\All Data 1201")
    dff = pd.DataFrame()
    for i in arr:
        zf = zipfile.ZipFile(f'C://Users//justi//Python Projects//PPP Analysis//PPP-Analysis//PPP Data//All Data 1201//{i}')
        file_list = zf.namelist()
        file_list = [k for k in file_list if '.csv' in k]
        file_list = [k for k in file_list if '_MACOSX' not in k]
        for j in file_list:
            df = pd.read_csv(zf.open(f'{j}'))
            dff = dff.append(df)

    dff = dff[dff['Zip'] == zipcode]

    dff = dff.merge(naics, on = 'NAICSCode')

    dff['Zip'] = dff['Zip'].apply(lambda x: str(x)[:-2])
    dff['Full_Address'] = dff['Address'] + ', ' + dff['City'] + ', ' + dff['State'] + ' ' + dff['Zip']

    return dff

if __name__ == '__main__':
    get_data_ready()