import sqlite3
connection= sqlite3.connect('todo.db')

connection.execute('create table student(roll int,subject text,city text,phone int)')
print("table student created")

connection.execute('insert into student(roll,subject,city,phone) values(34,"BEIT","Kathmandu",968000)')
connection.execute('insert into student(roll,subject,city,phone) values(35,"BCA","Kathmandu",968875400)')
connection.execute('insert into student(roll,subject,city,phone) values(36,"BESW","Gorkha",968457800)')

connection.commit()
print("Rows are inserted in Table student Created")

cursor=connection.cursor()
print("student info Created")
result= connection.execute('select * from student')
for rows in result:
    print(rows)
