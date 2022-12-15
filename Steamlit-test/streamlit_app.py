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
