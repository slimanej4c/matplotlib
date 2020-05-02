import mysql.connector
ls_people_index=[]
ls_people=[]
class sitedb:

    def __init__(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane'
        )
        cur=self.mydb.cursor()
        cur.execute('create database if not exists excel')


    def open_data(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='excel')
    def cpeople(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists people (id int(11) auto_increment primary key  ,fname varchar (25),lname varchar (25),age int(11))')
        self.mydb.close
        print("ok")
    def ipeople(self,fname,lname,age):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into people (fname,lname,age)values(%s,%s,%s)',(fname,lname,age))
        self.mydb.commit()
        self.mydb.close()
        print('iddd')

    def lspeople(self):

        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('select * from people ')
        sdate=cur.fetchall()
        for x in list(sdate):
            ls_people_index.append(x[0])
            ls_people.append(x[1:4])
        self.mydb.close()
go=sitedb()
go.cpeople()
#go.ipeople('khalil','beroual',31)
