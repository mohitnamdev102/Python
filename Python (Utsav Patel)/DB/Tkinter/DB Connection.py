import pymysql

db = pymysql.connect('localhost')

cursor = db.cursor()

sql = "SELECT VERSION()"

cursor.execute(sql)

a = cursor.fetchone()

print("Database Version is", a)

db.close()








