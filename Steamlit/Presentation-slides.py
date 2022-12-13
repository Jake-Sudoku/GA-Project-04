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

# Set Page configuration
# Read more at https://docs.streamlit.io/1.6.0/library/api-reference/utilities/st.set_page_config
st.set_page_config(page_title='Project 4 - West Nile Virus Prediction', page_icon='🦟', layout='wide', initial_sidebar_state='expanded')

# Set title of the app
st.title('🦟💀 Project 4 - West Nile Virus Prediction')

with st.sidebar:
    choose = option_menu("Overall", ["About", "Slides", "Interactive"],
                         icons=['house', 'people', 'file earmark slides', 'bar chart'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

#The "Overall" page
if choose == "Overall":
    col1 = st.columns( [0.8])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Overall about this project</p>', unsafe_allow_html=True)    

    
    st.write("This project is done to as part of General's Assembly (GA) requirement to pass the course. \nIt consist of the following sections : \n\nAbout \n\nSlides \n\nInteractive")    
    st.image(profile, width=700 )

#The "About" page
elif choose == "About":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About</p>', unsafe_allow_html=True)
    st.write("This project is done to as part of General's Assembly (GA) requirement to pass the course. \nIt consist of the following sections below : \n\nAbout \n\nSlides \n\nInteractive")    
    #st.image(profile, width=700 )

#The "Slides" page
elif choose == "Slides":
    def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    show_pdf('test-GA-Project-4.pdf')


elif choose == "Interactive":
    
    # Load data
    def data_train(): 
        df = pd.read_csv('./train_cleaned.csv')
        return df
    def data_spray(): 
        df = pd.read_csv('./spray_cleaned.csv')
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
    
