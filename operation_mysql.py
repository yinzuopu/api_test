#导入数据操作模块
import pymysql
#建立数据库链接
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123456",db="mysql",charset="utf8")
#建立游标
cur =conn.cursor()
#操作数据库
cur.execute("select * from student  where no =1")
#获取查询结果
result =cur.fetchall()
print(result)
#更新数据库
cur.execute("select * from student")
#输出全部结果
result1 =cur.fetchall()
print(result1)
#提交更改
conn.commit()
#关闭游标及链接
cur.close()
cur.close()