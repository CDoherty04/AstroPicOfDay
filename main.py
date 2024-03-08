import streamlit as st
import requests

# Use the requests library to access the API
url = "https://api.nasa.gov/planetary/apod?api_key=Ww4FeF3KFJkdazMivDlmKkCEhAvnovDDkm0sMrjN"
request = requests.get(url)
content = request.json()

# Set page layout and title
st.set_page_config(layout="wide", page_title="APOD")

# Write the title and credit at the top of the page
st.markdown("<h1 style='text-align: center;'>ASTRONOMY PICTURE OF THE DAY</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Using NASA's Open API</h3>", unsafe_allow_html=True)
st.markdown("***")

# Get the picture and description from NASA's Open API
st.image(content["hdurl"])
st.markdown(f"<p style='text-align: center;'>{content['explanation']}</p>", unsafe_allow_html=True)
st.markdown("***")
