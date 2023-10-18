import pandas as pd
from pathlib import Path
from base import Base
from to_mongo import ToMongo

# Set our folder directory
folder_dir = f'{Path(__file__).parents[0]}\\data'

# Create a csv file from the dataframe that we create in the base class:
Base().df.to_csv(f'{folder_dir}\\oracle_cards.csv', index = False)
print('Saved New Card Data to CSV File')

# Update the DataBase:
#ToMongo().drop_collection_dynamic
#ToMongo().upload_one_by_one
#print('Successfull Dropped all items in the Collection')
#print('Successfully Updated Collection with New Data')
# Read in the dataframe from the csv:
#df = pd.read_csv(f'{folder_dir}\\oracle_cards.csv', low_memory=False)
#print('Created the DataFrame object')

