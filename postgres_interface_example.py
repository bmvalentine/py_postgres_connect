# To use this module, you can create an instance of PostgresDatabase and pass 
# in the database name, user, password, host, and port. 
# You can then use the query() and insert() methods to execute SQL queries 
# and insert statements, respectively.
#
# This example was written by chatGBRT



db = PostgresDatabase(
    dbname="mydatabase",
    user="myusername",
    password="mypassword",
    host="localhost",
    port=5432
)

# Execute a query
result = db.query("SELECT * FROM mytable")
print(result)

# Insert a row into the database
values = ("John", "Doe", "johndoe@example.com")
db.insert("INSERT INTO mytable (first_name, last_name, email) VALUES (%s, %s, %s)", values)
