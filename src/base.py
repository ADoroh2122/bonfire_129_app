import requests
import pandas as pd

class Base:
    """
    Class that handles all connections to the API object and returns a DataFrame from it's initialization.

    Class has the following methods:
    return_url: returns the api_url we are currently working with
    get_data: scrapes the data from the API and creates a dataframe from it!

    """

    def __init__(self, url = 'https://api.scryfall.com/bulk-data'):
        self.api_url = url
        self.get_data()

    def get_data(self):
        '''Scrapes data from the API and creates a Dataframe from it'''
        self.df = pd.DataFrame.from_dict(requests.get(requests.get(self.api_url).json()['data'][0]['download_uri']).json())
        return self.df

if __name__ == '__main__':
    c = Base()
    print(c.df)