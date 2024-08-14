# pip install psycopg2-binary

dbname = 'dbname'
dbuser = 'dbuser'
dbpassword = 'dbpassword'
dbhost = 'dbhost'
dbport = 'dbport'

connection = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost, port=dbport)
cursor = connection.cursor()
query = "select * from table;"

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)
cursor.close()
connection.close()