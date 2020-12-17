import plotly.express as px
import pandas as pd

px.set_mapbox_access_token(open(".mapbox_token").read())

df = pd.DataFrame({'lat': [38.781609], 'long':[-77.237953]})

fig = px.scatter_mapbox(data_frame = df, lat = 'lat', lon='long')

fig.show()