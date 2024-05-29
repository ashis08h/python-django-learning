# pip install psycopg2-binary

dbname = 'db_name'
dbuser = 'db_user'
dbhost = 'db_host'
db_password = 'db_password'
db_port = 'db_port'

connection = psycopg2.connect(dbname=dbname, host=dbhost, user=dbuser, password=db_password, port=db_port)

cursor = connection.cusrsor()

query = 'SELECT * FROM Table_name;'

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
connection.close()