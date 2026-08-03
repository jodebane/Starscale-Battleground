import mysql.connector

# Establish connection to the database

connection = mysql.connector.connect(
        host="127.0.0.1",        
        user="root",    # Replace with your MySQL username
        password="",# Replace with your MySQL password
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

###test of function

cardsearch("starscale alpha")

