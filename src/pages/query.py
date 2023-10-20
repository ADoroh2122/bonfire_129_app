#imports first:

from pathlib import Path
import streamlit as st
import sys
import os

# Grab the filepath:
sys.path.insert(0, os.path.join(Path(__file__).parents[1]))

# Import Mongo Class:
from to_mongo import ToMongo

# Instantiate the class:
c = ToMongo()

# This will be the actual page:
st.header('Query Page')
st.write(
    '''
    This page will search our database for any card name you input! 
    
    Spelling of that name MUST BE EXACT
    
    '''
)

# Now we query the database
# Is to return information about a card from our database to a user in a friendly format
# Query the database off a user input, then display that info back to them!

# How can I use this in the future?
# When a user wants to query(or search) your database for information, we don't have to reference a local file anymore.
# We can plug and play a database in instead and allow a user to query that info back!

# When we build applications and dashboards, knowing how to allow a user to retrieve and view information is a powerful tool.

# How will we go about this???
# First, we will use the text_input function to allow a user to input a card name,
# Then, when we search the database for a match, we will return all the information that a user could need to know about a card.
# The .find() function will help us find all matches we need.

try:
    answer = st.text_input('Enter a Card Name:', value= 'Sol Ring')
    st.write(list(c.cards.find({'name' : answer})))

except:
    st.error('There was an issue with retrieving the card name you had input. Please double check that the spelling is exact!')
