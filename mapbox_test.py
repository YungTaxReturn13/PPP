import plotly.express as px
import pandas as pd

px.set_mapbox_access_token(open("PPP-Analysis\\Confidential\\.mapbox_token").read())

df = pd.DataFrame({'lat': [38.781609,38.792609], 'long':[-77.225953, -77.222953]})

fig = px.scatter_mapbox(data_frame = df, lat = 'lat', lon='long')

fig.show()