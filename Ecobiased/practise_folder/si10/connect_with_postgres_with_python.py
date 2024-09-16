# pip install psycopg2-binary
dbname = 'dbname'
dbuser = 'dbuser'
dbhost = 'dbhost'
dbport = 'dbport'
dbpassword = 'dbpassword'

connection = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost, port=dbport)

cursor = connection.cursor()
query = "select * from table_name;"

cursor.execute(query)
result =  cursor.fetchall()

for row in result:
    print(row)
cursor.close()
connection.close()
