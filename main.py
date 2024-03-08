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
st.markdown("<h4 style='text-align: center;'>Using NASA's Open API</h4>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{content['date']}</p>", unsafe_allow_html=True)
st.markdown("***")

# Get the title, picture, date, and description from NASA's Open API
st.markdown(f"<h2 style='text-align: center;'>{content['title']}</h2>", unsafe_allow_html=True)
st.markdown(f"<a style='text-align: center;'>{content['url']}</a>", unsafe_allow_html=True)
st.image(content["hdurl"])
st.markdown(f"<p style='text-align: center;'>{content['explanation']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Credits to: {content['copyright']}</p>", unsafe_allow_html=True)
st.markdown("***")
