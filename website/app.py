from os import write
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import streamlit.components.v1 as components
import hydralit as hy
from computervision.motiontracker import VideoTransformer
import pandas as pd
import numpy as np

app = hy.HydraApp(title='Head Tracker App')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

@app.addapp(title='Home')
def Home():
    st.title('Head Tracker')
    st.write('Accidents in roller coasters are still common in 2021. Therefore, the TEAM NAME came together to develop a Computer Vision software which has the objective of reducing the number of accidents in these rides: the Head Tracker.')

    st.subheader('1. What does the software do?')
    st.write('The Head Tracker is a system developed for theme parks to help prevent injuries in rollercoaster rides.')

    st.subheader('Software Specifications')
    st.write('was implemented using Computer Vision technology to . Through a Camera App, theme park staff can keep track of  Moreover, 3D model prototypes were designed for ')


@app.addapp(title='3D Models')
def Models():
    st.header("3D Model")
    st.write('3D modeling software: SolidWorks/Sketchfab')
    components.html(
        """
        <div class="sketchfab-embed-wrapper">
        <iframe title="Extreme Rusher coaster" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport
execution-while-not-rendered web-share src="https://sketchfab.com/models/c0000ad61af54e129aac616777a31f18/embed">
</iframe>
        <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;">
        <a href="https://sketchfab.com/3d-models/extreme-rusher-coaster-c0000ad61af54e129aac616777a31f18?utm_medium=embed&utm_campaign=share-popup&utm_content=c0000ad61af54e129aac616777a31f18"
target="_blank" style="font-weight: bold; color: #1CAAD9;"> Extreme Rusher coaster </a> by <a href="https://sketchfab.com/calbeluhn?utm_medium=embed&utm_campaign=share-popup&utm_content=c0000ad61af54e129aac616777a31f18"
target="_blank" style="font-weight: bold; color: #1CAAD9;"> c_albeluhn </a> on
        <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=c0000ad61af54e129aac616777a31f18"
target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a>
        </p>
        </div>
        """
    )

plot = st.empty()

@app.addapp(title='Demo')
def Demo():
    st.header("Demo")
    webrtc_streamer(key="demo",
                    video_transformer_factory=VideoTransformer)

    # Showcase data
    chart_data = pd.DataFrame(np.random.randn(20, 3),
                              columns=['a', 'b', 'c'])

    plot = st.line_chart(chart_data)




@app.addapp(title='About Us')
def Contact():
    st.header('Meet the Team')
    col1, col2 = st.columns(2)
    with col1:
        st.image("./img/bianca.jpg", width=300)
        st.write("Bianca Silva")
        st.write("Computer Engineering")
        st.write("Florida Polytechnic University")
        st.write("careerbiancasilva@gmail.com")

        st.image("./img/santiago.jpg", width=300)
        st.write("Santiago Gomez")
        st.write("Computer Science")
        st.write("Brigham Young University")
        st.write("gomezpaz@byu.edu")

    with col2:
        st.image("./img/chris.jpg", width=300)
        st.write("Christopher Molina")
        st.write("Computer Engineering")
        st.write("Florida Polytechnic University")
        st.write("christophermolina99@gmail.com")

        st.image("./img/kirill.jpg", width=300)
        st.write("Kirill Sokov")
        st.write("Mechatronic Engineering")
        st.write("Vaughn College of Aeronautics and Technology")
        st.write("kirill.sokolov124@gmail.com")

@app.addapp(title='Contact Us')
def Contact():
    st.header('Get in touch with us')
   
    ##link for Form Submit: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2Uyem5ldDJKVjRkaTBoTVJDRWNrUUZaWkhSZ3xBQ3Jtc0tsREpuSFdkbV9ENEFFUFNuNUlpZ3VsaVZWY1VLYl9PbHFFYnQtZk5pZnQtUjNQN1QzQ1NPNVUwcjFPWU9ONjVSQ1lVRmQxLXRKS1RHeVVmbVBieWxjU1RsVUlzNGtXM1Z4cGtLVHE1Z2hVbXYzZlZYWQ&q=https%3A%2F%2Fformsubmit.co%2F
    ##AFTER SETTING THE HEADER for contact us section

    contact_us = """
    <form action="https://formsubmit.co/cris23molina@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_us, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")
    


app.run()
