import numpy as np
import pandas as pd
import zipfile
import os
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
import base64
import plotly.graph_objs as go
from get_data_ready import get_data_ready

zipcode = 22152

dff = get_data_ready(zipcode)
#
# #Check to see if this zip code has already been made
# check = os.listdir(r'C:\Users\justi\Python Projects\PPP\PPP-Analysis\Coordinates')
# if (str(zipcode)+'.csv') in check:
#     coordinates = pd.read_csv(f'C:\\Users\\justi\\Python Projects\\PPP\\PPP-Analysis\\Coordinates\\{str(zipcode)}.csv')
# elif zipcode not in check:
#     get_coordinates(zipcode, dff)
#     coordinates = pd.read_csv(f'C:\\Users\\justi\\Python Projects\\PPP\\PPP-Analysis\\Coordinates\\{str(zipcode)}.csv')
# #Random Comments
# # image = r'C:\Users\justi\Python Projects\PPP\PPP-Analysis\crying-cat-meme-lede.jpg'
# # encode_image = base64.b64encode(open(image, 'rb').read()).decode('ascii')
# # pd.set_option('display.float_format', lambda x: '%.3f' % x)
# ###
#
#
# dff_industry = dff.groupby('2017 NAICS Title').sum().sort_values('LoanAmount',ascending=False)
#
# fig = px.bar(dff_industry.iloc[:10], x=dff_industry.index[:10], y='LoanAmount').update_xaxes(categoryorder="total descending")
# fig.update_layout(margin=dict(
#         l=10,
#         r=10,
#         b=200,
#         t=100,
#         pad=5),
#         xaxis_title="Industries",
#         title="Top 10 Industries sorted by total loan amount",
#         title_x=0.5)
# fig.update_xaxes(tickangle=25, tickfont=dict(size=14))
#
#
#
# app = dash.Dash()
# app.layout = html.Div(children=[
#     html.H1(children=f'Data of PPP Loans based on ZIP code: {zipcode}'),
#     html.Div(id='total_number'),
#     html.Div(id='total_amount'),
#     dcc.Graph(
#         id='industry_graph',
#         figure=fig),
#     html.Div(html.P([ html.Br()])),
#     html.H3(id="top"),
#     html.Div(children="Please enter how many loans you would like to see"),
#     dcc.Input(id='input', value='10', type='text'),
#     dash_table.DataTable(
#         id='datatable',
#         columns = [
#             {'name': i, 'id': i} for i in dff.columns],
#         data=dff.to_dict('records')
#     ),
#
#     html.Img(src='data:image/png;base64,{}'.format(encode_image),height=100,width=50)
# ])
#
# @app.callback(
#     [Output(component_id='total_number', component_property='children'),
#      Output(component_id='total_amount', component_property='children'),
#      Output(component_id='top', component_property='children'),
#      Output(component_id='datatable', component_property='data')],
#     [Input(component_id='input', component_property='value')])
# def update_values(input_data):
#
#     return (f"Total Number of Businesses within {zipcode}: {str(len(dff[dff['Zip']==int(zipcode)]))}", #Returns the total amount of businesses that recieved help in the zip
#             f"Total amount of money lent within {zipcode}: {round(dff[dff['Zip'] == int(zipcode)]['LoanAmount'].sum(),2):,}",
#             f"Top {input_data} Businesses that recieved PPP Loans by the amount recieved:",
#             dff.sort_values('LoanAmount',ascending=False)[:min(len(dff),int(input_data))].to_dict('records'))
#
#
#
#
# if __name__=="__main__":
#     app.run_server()
#
#
