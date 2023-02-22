import numpy as np
import pandas as pd
import streamlit as st
import random
import os
from PIL import Image

class RandomPicture():
    def __init__(self, directory):
        self.directory = directory
        self.extensions = ('.jpg', '.jpeg', '.png')
        self.last_file = None
        self.files = [f for f in os.listdir(directory) if f.endswith(self.extensions)]

    def get_random_picture(self):
        file = random.choice(self.files)
        while file == self.last_file and len(self.files)>1:
            self.files.remove(file)
            file = random.choice(self.files)
        self.last_file = file
        path = os.path.join(self.directory, file)
        return Image.open(path)

if __name__ == "__main__":
    picker = RandomPicture("C:/Users/Nikol/Carweb/ImageDownloader/images")
    image = picker.get_random_picture()  # Get a random picture

    st.set_page_config(page_title="Environment",
                           page_icon=":fox:",
                           layout="wide",
                           )

    tab1, tab2 = st.tabs(["Foxes", "More foxes"])

    with tab1:
            st.header("Fox")
            button1 = st.button('Press me?')

    if button1:
            st.write("Button clicked")
            st.image(image, caption='Random Image', use_column_width=True)

    else:
            st.write("Button not clicked")

    with tab2:
            st.header("More foxes")
            st.image(image, caption='Sunrise by the mountains')






picker = RandomPicture("C:/Users/Nikol/Carweb/ImageDownloader/images")

image = picker.get_random_picture()  # Get a random picture




