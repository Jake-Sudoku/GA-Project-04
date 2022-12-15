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

# Set Page configuration
# Read more at https://docs.streamlit.io/1.6.0/library/api-reference/utilities/st.set_page_config
st.set_page_config(page_title='Project 4 - West Nile Virus Prediction', page_icon='🦟', layout='wide', initial_sidebar_state='expanded')

# Set title of the app
st.title('🦟💀 Project 4 - West Nile Virus Prediction')


with st.sidebar:
    choose = option_menu("Directory",[ "About","Slides", "Interactive"],
                         icons=['people', 'file earmark slides', 'bar-chart'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )


st.markdown(""" <style> .font {
font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
 </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">About</p>', unsafe_allow_html=True)
st.write("This project is done to as part of General's Assembly (GA) requirement to pass the course. \nOur Group Members : \n\nTan Ming Jie \n\nLiam Ting Wei \n\nMaryam \n\nPriscilla Ong \n\nJimmy Ong")    
#st.image(profile, width=700 )
st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
