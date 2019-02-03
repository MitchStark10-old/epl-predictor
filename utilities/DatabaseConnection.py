import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(user='waterman73', password='Q7uq8q5e',
                                host='nerdnite.cp5wcakjnkdt.us-east-2.rds.amazonaws.com',
                                database='nerdnite')

    def retrieveDbConnection(self):
        return self.connection