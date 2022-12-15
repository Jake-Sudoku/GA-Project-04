# Import Libraries
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import pandas as pd
import numpy as np
import time 
import plotly.express as px
from plotly.offline import iplot
from  PIL import Image
import cv2
import io
import base64
from pathlib import Path

# Set Page configuration
# Read more at https://docs.streamlit.io/1.6.0/library/api-reference/utilities/st.set_page_config
st.set_page_config(page_title='Number of Mosquitos in areas with wnvpresent', page_icon='🦟', layout='wide', initial_sidebar_state='expanded')

# Set title of the app
st.title('🦟💀 Project 4 - West Nile Virus Prediction')

# Load data
df_train_csv = Path(__file__).parents[0] / 'train_cleaned.csv'
df_spray_csv = Path(__file__).parents[0] / 'spray_cleaned.csv'

# Load data
df_train = pd.read_csv(df_train_csv)
df_spray = pd.read_csv(df_spray_csv)

#Number of Mosquitos in areas with wnvpresent
MAPBOX_TOKEN = 'pk.eyJ1IjoibWFyaWVkcmV6IiwiYSI6ImNsOXl5dTFtZjAyYm4zd28zN3Y1ZzYycm0ifQ.W1Toe6X5S9AELY56h0OQDw'
px.set_mapbox_access_token(MAPBOX_TOKEN)

#Count the number of mosquitos in areas
mosquito_count = df_train.groupby(['address'], as_index = False)[['nummosquitos']].sum()
#Group the area by address and use the median address
areas = df_train.groupby(['address'], as_index = False)[['latitude','longitude']].median()

#Group the wnvpresent by address
wnv = df_train.groupby(['address'], as_index = False)[['wnvpresent']].sum() 

#Merge mosquitocount , areas and wnvpresent together
mosquito_areas_wnv = pd.concat([mosquito_count,areas, wnv], axis = 1)

#Drop the address as it is not required
mosquito_areas_wnv.drop('address', axis = 1, inplace = True)

fig = px.scatter_mapbox(mosquito_areas_wnv, lat = 'latitude', lon  = 'longitude', color = 'wnvpresent',
                        size = 'nummosquitos', color_continuous_scale=px.colors.cyclical.Edge,
                        hover_data = ['nummosquitos', 'wnvpresent'],
                       zoom = 9,mapbox_style="light",
                       title="Number of Mosquitos in areas with wnvpresent")

fig.show()
st.plotly_chart(fig, use_container_width=True)

fig1 = px.scatter_mapbox(mosquito_areas_wnv, lat = 'latitude', lon  = 'longitude', color = 'wnvpresent',
                        size = 'nummosquitos', color_continuous_scale=px.colors.cyclical.Edge,
                        hover_data = ['nummosquitos', 'wnvpresent'],
                       zoom = 9,mapbox_style="open-street-map",
                       title="Number of Mosquitos in areas with wnvpresent")

fig1.show()
st.plotly_chart(fig1, use_container_width=True)
