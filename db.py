import pandas as pd
import os
from datetime import datetime

class Database:
    def __init__(self):
        if os.path.isfile('./Database.csv'):
            self.backupDB()
        self.db = pd.DataFrame({},columns = ['page', 'idx', 'year', 'method', 'area', 'st_price', 'final_price', 'auction_year', 'auction_month', 'auction_date'])

    def backupDB(self):
        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")
        print(os.path)
        os.rename('./Database.csv', f'./Database_backup_{date_time}.csv')

    def openDB(self):
        self.db = pd.read_csv('Database.csv')

    def saveDB(self):
        self.db.to_csv("Database.csv")

    def getID(self, id):
        str_data = self.db.loc[id]
    
    def deleteID(self, id):
        self.db.drop(id, axis=0, inplace=True)
    
    def saveID(self, id, data):
        self.db.loc[id] = data

    def updateID(self, id, data):
        self.db.loc[id] = data


if __name__ == "__main__":
    tmp_class = Database()
    

