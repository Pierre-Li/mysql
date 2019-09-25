from mySql import mySql

s = mySql("localhost", "root", "10251206", "li_1")

res = s.get_all("select * from bandcard where money>400")

for row in res:
    print("%d--%d" % (row[0], row[1]))