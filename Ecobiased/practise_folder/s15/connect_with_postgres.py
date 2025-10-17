# pip install binary-psycopg2

dbname = 'dbname'
dbuser = 'dbuser'
dbpassword = 'dbpassword'
dbhost = 'dbhost'
dbport = 'dbport'

connection = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost, port=dbport)

cursor = connection.cursor()

query = "select * from table_name"

cursor.execute(query)

result = cursor.fetchall()
print(result)

for row in result:
    print(row)

cursor.close()
connection.close()