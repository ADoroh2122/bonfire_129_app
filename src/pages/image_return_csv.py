# Imports for the image return page
import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO
import pandas as pd

folder_dir = os.path.join(Path(__file__).parents[1], 'data')

df = pd.read_csv(f'{folder_dir}\\oracle_cards.csv', low_memory=False)

# When I go to click on the page:
st.title("Image Return Page")

# Then we take an input from the user:
answer = st.text_input("Enter a Card Name:", value = 'Sol Ring')

# Transform that into a query!
card = df[df['name'] == answer]['image_uris']
print(card)
# st.image(Image.open(BytesIO(requests.get(card).content)))
