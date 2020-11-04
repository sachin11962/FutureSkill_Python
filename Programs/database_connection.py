import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="telusko")

mycursor = mydb.cursor()

# mycursor.execute("show databases")
#
# for i in mycursor:
#     print(i)

mycursor.execute("show databases")
result = mycursor.fetchall()
for i in result:
    print(i)

mycursor.execute("select * from student")

for i in mycursor:
    print(i)