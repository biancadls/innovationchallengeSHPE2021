# Create website using streamlit

import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import streamlit.components.v1 as components


st.title("Head Tracker")
st.header("Data")

st.header("3D Model")
components.html(
    """
    <div class="sketchfab-embed-wrapper"> 
    <iframe title="Pumpkin Girl" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/4d7df77e7a7647e09eadbf57a512e246/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/pumpkin-girl-4d7df77e7a7647e09eadbf57a512e246?utm_medium=embed&utm_campaign=share-popup&utm_content=4d7df77e7a7647e09eadbf57a512e246" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Pumpkin Girl </a> by <a href="https://sketchfab.com/martaesz?utm_medium=embed&utm_campaign=share-popup&utm_content=4d7df77e7a7647e09eadbf57a512e246" target="_blank" style="font-weight: bold; color: #1CAAD9;"> martaesz </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=4d7df77e7a7647e09eadbf57a512e246" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p>
    </div>
    """
)

st.header("Demo")
webrtc_streamer(key="example")
