import streamlit as st
import requests

# Set page layout and title
st.set_page_config(layout="wide", page_title="APOD")

# Get the picture and description from NASA's Open API
picture = ""
description = ""

# Write the title and credit at the top of the page
st.markdown("<h1 style='text-align: center;'>ASTRONOMY PICTURE OF THE DAY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Using NASA's Open API</p>", unsafe_allow_html=True)

# Write the picture and description
# st.image(picture)
st.markdown("***")
st.markdown(f"<p style='text-align: center;'>{description}</p>", unsafe_allow_html=True)
