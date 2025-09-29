import psycopg2#Import the module

connection = psycopg2.connect( #All required for connecting to a db
    dbname= 'postgres',
    user= 'mark',
    password= '1234@hokage',
    host= 'localhost',
    port= '5432'
)

cur = connection.cursor()

connection.commit()
cur.close()
connection.close()
#The above 3 lines are a must as they close the connection but mostly cause we need them.