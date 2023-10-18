from base import Base
import pymongo
import os
from dotenv import load_dotenv

# Class Declaration:
class ToMongo(Base):
    '''
    Designed as a class to transport the data from our Base class to a MongoDB instance.
    Initilaizes an instance of the inherited class.

    Defined methods are as follows:
    upload_one_by_one: Upload pieces of information to a database one by one over an iterable structure.
    upload_collection: Uploads an entire collection of documents to MongoDB.
    delete_collection: Drops an entire collection of data from the database.
    '''

    def __init__(self):
        # Initialize an instance of our inherited class:
        Base.__init__(self)
        # Load in the env variables:
        load_dotenv()
        self.__mongo_url = os.getenv('MONGO_URL') 
        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.__mongo_url)
        # Create/Connect to the database
        self.db = self.client.db
        # Create/Connect to a collection:
        self.cards = self.db.cards
        # Set the DataFrame index to the ID Column:
        self.df.set_index('id', inplace = True)

    def upload_one_by_one(self):
        '''
        Upload all our items in the dataframe to MongoDB one-by-one
        This method will take longer, but will ensure all our data is correctly uploaded!
        '''

        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())

    def upload_collection(self):
        '''
        Upload an entire collection of documents to MongoDB.
        BEWARE! THERE IS A MAXIMUM UPLOAD SIZE!!
        Limitations are placed on the amount of data that you can upload at one time!
        '''

        self.cards.insert_many([self.df.to_dict()])

    def drop_collection(self):
        self.db.cards.drop()

    def drop_collection_dynamic(self, col_name:str='cards'):
        self.db.drop_collection(col_name)

if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.drop_collection_dynamic()
    print('Dropped the Cards Collection')
    c.upload_one_by_one()
    print('Successfull Uploaded all Card Info to MongoDB!')