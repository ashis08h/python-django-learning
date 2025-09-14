# pip install binary-psycopg2

dbname = "dbname"
dbuser = "dbuser"
dbhost = "dbhost"
dbport = "dbport"
dbpassword = "dbpassword"


connection = psycopg2.connect(dbname=dbname, user=dbuser, port=dbport, host=dbhost, password=dbpassword)
cursor = connection.cursor()

query = "select * from table_name;"

cursor.execute(query)
result = cursor.fetchall()
print(result)

for row in result:
    print(row)

cursor.close()
connection.close()
