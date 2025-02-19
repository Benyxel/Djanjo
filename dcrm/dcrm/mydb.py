import mysql.connector 
import mysql.connector 

# Connect to MySQL server without specifying a database
database = mysql.connector.connect(
    host="localhost",
    user="root",    # root
    password="GiftyNarh@2025"
)

cursorObject = database.cursor()

# Create the database if it doesn't exist
cursorObject.execute("CREATE DATABASE IF NOT EXISTS benyxel")

# Connect to the newly created database
database = mysql.connector.connect(
    host="localhost",
    user="root",    # root
    password="GiftyNarh@2025",
    database="benyxel"
)

cursorObject = database.cursor()

print("All Done!")