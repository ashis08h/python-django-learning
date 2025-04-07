# pip install binary-pyscopg2

dbname = "dbname"
dbuser = "user"
dbpassword = "password"
dbhost = "host"
dbport = "port"


connection = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost, port=dbport)
cursor = connection.cursor()

query = "select * from table;"

cursor.execute(query)
result = cursor.fetchall()
print(result)

for row in result:
    print(row)

cursor.close()
connection.close()