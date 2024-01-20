# pip install psycopg2-binary

db_name = 'db_name'
db_user = "db_user"
db_password = "db_password"
db_host = "host"
db_port = "port"

connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)

cursor = connection.cursor()

query = "SELECT * FROM table_name"

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()