import pymysql

db = pymysql.connect("localhost", "root", "10251206", "li_1")

cursor = db.cursor()

sql = "update bandcard set money=1000 where id=1"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
