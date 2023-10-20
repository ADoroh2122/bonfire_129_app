# Imports for the image return page
import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO

# Create the filepath to the system where the main folder for the application lives:
sys.path.insert(0,os.path.join(Path(__file__).parents[1]))

# Import the created class from our file
from to_mongo import ToMongo


# When I go to click on the page:
st.title("Image Return Page")

# Create an instance of our Mongo Class:
c = ToMongo()

# Then we take an input from the user:
answer = st.text_input("Enter a Card Name:", value='Sol Ring')

# Transform that into a query!
card = list(c.cards.find({'name':answer}))[0]['image_uris']['normal']
st.image(Image.open(BytesIO(requests.get(card).content)))