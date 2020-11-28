#另一种封装方法
#导入pymysql库
import pymysql
class DB:
    def __init__(self):
        self.conn =pymysql.connect(host="127.0.0.1",
                                   port=3306,
                                   user="root",
                                   passwd="123456",#注意是passwd不是password
                                   db="mysql")
        self.cur =self.conn.cursor()

    def __del__(self):#分析函数，实施删除时触发
        self.cur.close()
        self.conn.close()

    def query(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self,name):
        result = self.query("select *  from student where name ='{}'".format(name))
        return True if result else False

    def del_user(self,name):
        self.exec("delete from student where name ='{}'".format(name))


