import pymysql
db = pymysql.connect('localhost', 'root', '', 'chitti')
cursor = db.cursor()

# sql = "CREATE TABLE `employe`(`id` INT(), `name` VARCHAR(40), `age` INT(), PRIMARY KEY(`id`))"
sql = "CREATE TABLE `employee` ( `id` INT NOT NULL , `name` VARCHAR(40) NOT NULL , `age` INT NOT NULL , PRIMARY KEY(`id`));"
try:
    cursor.execute(sql)
    db.commit()
    print("success")

except Exception as e:
    print("Error:", e)
    db.rollback()


db.close()