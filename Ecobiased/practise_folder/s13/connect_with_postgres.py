# pip install binary-psycopg2

dbname = "dbname"
dbuser = "dbuser"
dbhost = "dbhost"
dbport = "dbport"
dbpassword = "dbpassword"

connection = psycopg2.connect(dbname=dbname, user=dbuser, host=dbhost, port=dbport, password=dbpassword)
cursor = connection.cursor()

query = "select * from table;"

cursor.execute(query)
result = cursor.fetchall()
print(result)

for row in result:
    print(row)

cursor.close()
connection.close()