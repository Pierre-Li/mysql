"""
fetchone()
获取下一个查询结果集，结果是一个对象

fetchall()
接受全部的返回行

rowcount:是一个只读属性，返回excute()方法影响的行数
"""
import pymysql

db = pymysql.connect("localhost", "root", "10251206", "li_1")

cursor = db.cursor()

sql = "select * from bandcard where money>400"
try:
    cursor.execute(sql)
    reslist = cursor.fetchall()
    for row in reslist:
        print("%d--%d" % (row[0], row[1]))
except:
    db.rollback()

cursor.close()
db.close()
