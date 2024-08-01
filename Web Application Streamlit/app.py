import streamlit as st
from streamlit_option_menu import option_menu
import home, prediction, visualization, powerbi, about
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title= "Machine Predictive Maintenance",
    page_icon= ":Bar_chart",
    layout="wide"
)

class MultiApp:
    def __init__(self):
        self.apps= []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Navigation",
                options=['Home', 'Prediction', 'Visualization', 'Power BI', 'About'],
                icons=['person-circle', 'house-fill', 'person-circle', 'person-circle', 'person-circle'],
                menu_icon='chat-text-fill',
                default_index=0
            )
        
            

        if app == 'Home':
            home.app()

        if app == 'Prediction':
            prediction.show_prediction_page()

        if app == 'Visualization':
            visualization.show_visualization_page()
            

        if app == 'Power BI':
            powerbi.app()

        if app == 'About':
            about.app()

    run()
