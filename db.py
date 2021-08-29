import pandas as pd
import os.path

class Database:
    def __init__(self):
        # if os.path.isfile('./Database.csv'):
        #     self.openDB()
        # else:
        self.db = pd.DataFrame({},columns = ['page', 'idx', 'year', 'method', 'area', 'st_price', 'final_price', 'auction_year', 'auction_month', 'auction_date'])

    def openDB(self):
        self.db = pd.read_csv('Database.csv')

    def saveDB(self):
        self.db.to_csv("Database.csv")

    def getID(self, id):
        str_data = self.db.loc[id]        
        return str_data
    
    def deleteID(self, id):
        self.db.drop(id, axis=0, inplace=True)
        self.saveDB()
    
    def saveID(self, id, data):
        self.db.loc[id] = data
        self.saveDB()

    def updateID(self, id, data):
        self.db.loc[id] = data
        self.saveDB()



    

