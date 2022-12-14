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

elif choose == "Interactive":
    @st.cache
    # Load data
    def data_train(): 
        df = pd.read_csv('train_cleaned.csv')
        return df
    def data_spray(): 
        df = pd.read_csv('spray_cleaned.csv')
        return df

    df_train=data_train()
    df_spray=data_spray()

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
    
    
    #Traps Locations from 2007-2013
    MAPBOX_TOKEN = 'pk.eyJ1IjoibWFyaWVkcmV6IiwiYSI6ImNsOXl5dTFtZjAyYm4zd28zN3Y1ZzYycm0ifQ.W1Toe6X5S9AELY56h0OQDw'
    px.set_mapbox_access_token(MAPBOX_TOKEN)
    fig = px.scatter_mapbox(df_train, lat = 'latitude', lon  = 'longitude',animation_frame="date",size_max=15, zoom = 10)

    fig.update_layout(title = 'Traps Locations from 2007-2013',
    autosize=False,
    width=500,
    height=700,)

    fig.show()
    st.plotly_chart(fig, use_container_width=True)