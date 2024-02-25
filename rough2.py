import streamlit as st
from streamlit_option_menu import option_menu
import subprocess

selected = option_menu(
    'Choose Disease Prediction Model',
    ['Home','Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lungs Cancer Prediction'],
    menu_icon='hospital-fill',
    icons=['person','activity','heart', 'activity','lungs'],
    default_index=0
)


# def create_navigation_bar(options):
#     selected_option = option_menu(
#         menu_title=None,
#         options=options,
#         icons=["house", "book", "envelope"],
#         menu_icon="cast",
#         orientation="horizontal",
#         styles={
#             "container": {"padding": "20px", "background-color": "#333", "display": "flex", "justify-content": "space-between"},
#             "icon": {"color": "orange", "font-size": "25px"},
#             "nav-link": {"font-size": "16px", "color": "white", "text-align": "left", "margin": "0px", "padding": "10px", "text-decoration": "none", "transition": "0.3s", "display": "inline-block"},
#             "nav-link:hover": {"background-color": "#555", "text-decoration": "none"},
#             "nav-link-selected": {"background-color": "green"}
#         }
#     )
#     return selected_option

# def website():
#     options = ['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lungs Cancer Prediction']
#     selected_page = create_navigation_bar(options)

#     if selected_page == "Home":
#         subprocess.Popen(["streamlit", "run", "Govind.py"])
#         # Add content for the Home page
#     elif selected_page == "Diabetes Prediction":
#         subprocess.Popen(["streamlit", "run", "Govind_Diabetes.py"])
#         # Add content for the Diabetes Prediction page
#     elif selected_page == "Parkinsons Prediction":
#         subprocess.Popen(["streamlit", "run", "Govind_Parkinson.py"])
#         # Add content for the Parkinsons Prediction page
#     elif selected_page == "Lungs Cancer Prediction":
#         subprocess.Popen(["streamlit", "run", "Govind_Lungs.py"])
#         # Add content for the Lungs Cancer Prediction page

# if __name__ == "__main__":
#     website()
