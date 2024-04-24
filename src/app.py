"""
    Azure Streamlit Demo
    Author: Alexander Bieniek
    Inspiration: Wolf Paulus (wolf@paulus.com), ChatGPT
    streamlit run src/app.py
    Program displays movie posters and an accompanying link to the movies' wikipedia
"""

from io import BytesIO
import streamlit as st
from PIL import Image
import requests

def ui() -> None:
    st.title("Good Movies Demo on Streamlit")
    st.subheader(".. Almost on Azure")

ui()

if __name__ == "__main__":
    #image_path1 = "C:\\Users\\awbie\\Visual Studio Code Projects\\CS399_Module8_Homework\\cicd24\\images\\Hitchhikers_guide_to_the_galaxy.jpg"
    image_path1 = requests.get("https://raw.githubusercontent.com/BOBBLE22/cicd24/main/images/Hitchhikers_guide_to_the_galaxy.jpg")
    #image1 = Image.open(image_path1)
    if image_path1.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(image_path1.content))
    
        # Display the image using Streamlit
        st.image(image, caption="The Hitchhiker's Guide to the Galaxy released 2005", use_column_width=15)
        url1 = "https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy_(film)"
        st.link_button("Visit Hitchhikers Guide to the Galaxy wiki", url1)
    else:
        st.write("Failed to retrieve the image")
    
    #image_path2 = "C:\\Users\\awbie\\Visual Studio Code Projects\\CS399_Module8_Homework\\cicd24\\images\\Aliens_poster.jpg"
    image_path2 = requests.get("https://raw.githubusercontent.com/BOBBLE22/cicd24/main/images/Aliens_poster.jpg")
    #image2 = Image.open(image_path2)
    if image_path2.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(image_path2.content))
    
        # Display the image using Streamlit
        st.image(image, caption="Aliens released 1986", use_column_width=15)
        url2 = "https://en.wikipedia.org/wiki/Aliens_(film)"
        st.link_button("Visit Aliens wiki", url2)
    else:
        st.write("Failed to retrieve the image")
    
    #image_path3 = "C:\\Users\\awbie\Visual Studio Code Projects\\CS399_Module8_Homework\\cicd24\\images\\Spaceballs.jpg"
    image_path3 = requests.get("https://raw.githubusercontent.com/BOBBLE22/cicd24/main/images/Spaceballs.jpg")
    if image_path3.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(image_path3.content))
    
        # Display the image using Streamlit
        st.image(image, caption="Spaceballs released 1987", use_column_width=15)
        url3 = "https://en.wikipedia.org/wiki/Spaceballs"
        st.link_button("Visit alls wiki", url3)
    else:
        st.write("Failed to retrieve the image")

