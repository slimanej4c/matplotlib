import mysql.connector
ls_id=[]

class sitedb:

    def __init__(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane'
        )
        cur=self.mydb.cursor()
        cur.execute('create database if not exists test_excel')


    def open_data(self):
        self.mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='slimane',
            database='test_excel')
    def ctable1(self):
        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('create table if not exists table1(id varchar(50) primary key  ,role varchar (100),'
                    'Related_ASPICE_Sub_Process varchar (100),'
                    'Activity_category_TOPIC_CLEM1 varchar (100),Activity_Description_ASWP1 varchar (100),'
                    'Related_ASWP_Sub_Process1 varchar(100),CO1 varchar(1600),Workproduct1 varchar(100),'
                    'Activity_category_TOPIC_CLEM2 varchar(100),Activity_Description_ASWP2 varchar(100),'
                    'Related_ASWP_Sub_Process2 varchar(100),CO2 varchar(1600),Workproduct2 varchar(140))')
        self.mydb.close

    def itable1(self,id ,role,Related_ASPICE_Sub_Process,Activity_category_TOPIC_CLEM1,Activity_Description_ASWP1,Related_ASWP_Sub_Process1,CO1,Workproduct1,Activity_category_TOPIC_CLEM2,Activity_Description_ASWP2,Related_ASWP_Sub_Process2,CO2,Workproduct2):
        self.open_data()
        cur = self.mydb.cursor()
        cur.execute('insert into table1 (id ,role,Related_ASPICE_Sub_Process,'
                    'Activity_category_TOPIC_CLEM1,Activity_Description_ASWP1,'
                    'Related_ASWP_Sub_Process1,CO1,Workproduct1,Activity_category_TOPIC_CLEM2,Activity_Description_ASWP2,'
                    'Related_ASWP_Sub_Process2,CO2,Workproduct2)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(id ,role,Related_ASPICE_Sub_Process ,Activity_category_TOPIC_CLEM1,Activity_Description_ASWP1,Related_ASWP_Sub_Process1,CO1,Workproduct1,Activity_category_TOPIC_CLEM2,Activity_Description_ASWP2,Related_ASWP_Sub_Process2,CO2,Workproduct2))
        self.mydb.commit()
        self.mydb.close()


    def lsid(self):

        self.open_data()
        cur=self.mydb.cursor()
        cur.execute('select id from table1')
        sid=cur.fetchall()
        for x in list(sid):
            ls_id.append(x[0])

        self.mydb.close()

    def utable1(self,id ,role,Related_ASPICE_Sub_Process,Activity_category_TOPIC_CLEM1,
               Activity_Description_ASWP1,Related_ASWP_Sub_Process1,CO1,Workproduct1,
               Activity_category_TOPIC_CLEM2,Activity_Description_ASWP2,Related_ASWP_Sub_Process2,
               CO2,Workproduct2):

        self.open_data()
        cur = self.mydb.cursor()
        cur.execute("update table1 set role =%s,Related_ASPICE_Sub_Process=%s,Activity_category_TOPIC_CLEM1=%s,"
                    "Activity_Description_ASWP1=%s,Related_ASWP_Sub_Process1=%s,CO1=%s,Workproduct1=%s,"
                    "Activity_category_TOPIC_CLEM2=%s,Activity_Description_ASWP2=%s,Related_ASWP_Sub_Process2=%s,"
                    "CO2=%s,Workproduct2=%s where id=%s",(role,Related_ASPICE_Sub_Process,Activity_category_TOPIC_CLEM1,
               Activity_Description_ASWP1,Related_ASWP_Sub_Process1,CO1,Workproduct1,
               Activity_category_TOPIC_CLEM2,Activity_Description_ASWP2,Related_ASWP_Sub_Process2,
               CO2,Workproduct2,id))
        self.mydb.commit()
        self.mydb.close()

