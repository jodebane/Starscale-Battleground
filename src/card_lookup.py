

import mysql.connector
from mysql.connector import Error

# Establish connection to the database

connection = mysql.connector.connect(
        host="127.0.0.1",        
        user="root",    # Replace with your MySQL username
        password="CatsAreSupreme101",# Replace with your MySQL password
        database="ssbg_cards" # Replace with your target database name
    )

if connection.is_connected():
        print("Successfully connected to MySQL database!")

###function to see info on a card in the database
def cardsearch(cardname):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM base_cards_list WHERE Name = %s", (cardname,))
    myresult = cursor.fetchall()
    print(myresult)

cardsearch("starscale alpha")

decklist = ["Starscale alpha", "starscale alpha", "militia infantry", "space pirate hideaway"]

def decklistsearch(v):
    for i in range(0, len(v)):
         cardsearch(v[i])

decklistsearch(decklist)