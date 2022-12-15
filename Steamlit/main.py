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


#Path finder
df_train_csv = Path(__file__).parents[0] / '00-Datasets/train_cleaned.csv'
df_spray_csv = Path(__file__).parents[0] / '00-Datasets/spray_cleaned.csv'
slides_pdf = Path(__file__).parents[0] / 'test-GA-Project-4.pdf'

#Load data
df_train = pd.read_csv(df_train_csv)
df_spray = pd.read_csv(df_spray_csv)

#Set map token
MAPBOX_TOKEN = 'pk.eyJ1IjoibWFyaWVkcmV6IiwiYSI6ImNsOXl5dTFtZjAyYm4zd28zN3Y1ZzYycm0ifQ.W1Toe6X5S9AELY56h0OQDw'
px.set_mapbox_access_token(MAPBOX_TOKEN)

#Set data and values before ploting
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


# Set Page configuration
st.set_page_config(page_title='Project 4 - West Nile Virus Prediction', page_icon='🦟', layout='wide', initial_sidebar_state='expanded')

# Set title of the app
st.title('🦟💀 Project 4 - West Nile Virus Prediction')

with st.sidebar:
    choose = option_menu("Directory",[ "About👦👨👨👩👩","🦟🦟🦟Mosquito Clusters🦟🦟🦟", "☠️🦟Spray🦟☠️"],
                         icons=['people', 'bar-chart', 'bar-chart'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

#The "About" page
if choose == "About👦👨👨👩👩":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About</p>', unsafe_allow_html=True)
    st.write("This project is done to as part of General's Assembly (GA) requirement to pass the course. \n\nDSI33 Group Members : \n\nTan Ming Jie \n\nLiam Ting Wei \n\nMaryam \n\nPriscilla Ong \n\nJimmy Ong")    
    #st.image(profile, width=700 )

#The Mosquito cluster page
elif choose == "🦟🦟🦟Mosquito Clusters🦟🦟🦟":
    fig = px.scatter_mapbox(mosquito_areas_wnv, lat = 'latitude', lon  = 'longitude', color = 'wnvpresent',
                            size = 'nummosquitos', color_continuous_scale=px.colors.cyclical.Edge,
                            hover_data = ['nummosquitos', 'wnvpresent'],
                           zoom = 9,mapbox_style="light",
                           title="Number of Mosquitos in areas with wnvpresent")

    fig.show()
    st.plotly_chart(fig, use_container_width=True)

#
elif choose == "☠️🦟Spray🦟☠️":
    fig1 = px.scatter_mapbox(df_spray, lat = 'latitude', lon  = 'longitude',
                        size_max=15, zoom = 9,color_discrete_sequence=["olive"],  opacity = 0.5,mapbox_style="light")

    fig2 = px.scatter_mapbox(mosquito_areas_wnv, lat = 'latitude', lon  = 'longitude', color = 'wnvpresent',
                        size = 'nummosquitos', color_continuous_scale=px.colors.cyclical.Twilight,
                        hover_data = ['nummosquitos', 'wnvpresent'])

    fig1.add_trace(fig2.data[0],)

    fig1.update_layout( title = 'Spray relationship with Virus and Mosquito clusters')
    st.plotly_chart(fig1, use_container_width=True)
