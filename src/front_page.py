import streamlit as st

st.title("Bonfire-129 MTG Tracer Application")
st.text('My first application that utilizes Pandas, Streamlit, SkLearn, SpaCy, MongoDB, Plotly, and Python to creat a MTG Recommendation System')

st.header('Here are the different pages of my application:')
st.subheader('Image Return:')
st.text('Image Return: Returns an image of the requested card')

st.subheader('Summary:')
st.text('Summary Page, ecplaining all the inner workings of my application and th "why" behind decisions we made!')

st.subheader('Query')
st.text('Query: Allows a user to enter a card name and queries the database in mongo for all information matching that card name. Card names MUST be exact')

st.subheader('Recommender')
st.text('A recommendation system that we will build to allow users to see recommended cards')

st.subheader('Vis')
st.text('Vis: Ability to create a couple of visualizations using Plotly')