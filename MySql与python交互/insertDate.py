import pymysql

db = pymysql.connect("localhost", "root", "10251206", "li_1")

cursor = db.cursor()

sql = "insert into bandcard value(0,100)"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
