import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',passwd='')

print(conn)

cursor = conn.cursor()

try:
	dbs = cursor.execute("SHOW DATABASES")

except:
	print("Exception occur")

for i in dbs:
	print(i)

conn.close()