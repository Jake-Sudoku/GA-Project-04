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
st.set_page_config(page_title='Project 4 - West Nile Virus Prediction', page_icon='🦟', layout='wide', initial_sidebar_state='expanded')

# Set title of the app
st.title('🦟💀 Project 4 - West Nile Virus Prediction')




# Load data
df_train_csv = Path(__file__).parents[0] / 'train_cleaned.csv'
df_spray_csv = Path(__file__).parents[0] / 'spray_cleaned.csv'


# Load data
df_train = pd.DataFrame(df_train_csv)
df_spray = pd.DataFrame(df_spray_csv)

#Spray Locations from 2011-2013
MAPBOX_TOKEN = 'pk.eyJ1IjoibWFyaWVkcmV6IiwiYSI6ImNsOXl5dTFtZjAyYm4zd28zN3Y1ZzYycm0ifQ.W1Toe6X5S9AELY56h0OQDw'
px.set_mapbox_access_token(MAPBOX_TOKEN)
fig = px.scatter_mapbox(df_spray, lat = 'latitude', lon  = 'longitude',animation_frame="date",size_max=15, zoom = 10)

fig.update_layout(title = 'Spray Locations from 2011-2013',
                  autosize=False,
                  width=500,
                  height=700,
                  mapbox_accesstoken=MAPBOX_TOKEN,mapbox_style="light")
fig.show()
st.plotly_chart(fig, use_container_width=True)
    
    
