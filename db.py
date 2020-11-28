# 导入第三方模块
import pymysql


# 获取链接方式from pymysql.connections import Connection


def get_db_conn():
    conn = pymysql.connect ( host="127.0.0.1",
                             port=3306,
                             user="root",
                             password="123456",
                             db="mysql",
                             charset="utf8" )
    return conn


# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn ()
    cur = conn.cursor ()
    cur.execute ( sql )
    result = cur.fetchall ()
    cur.close ()
    conn.close ()
    return result


# 封装数据库更改操作
def change_db(sql):
    conn = get_db_conn ()
    cur = conn.cursor ()
    try:
        cur.execute ( sql )
        conn.commit ()
    except Exception as e:
        conn.rollback ()
    finally:
        cur.close ()
        conn.close ()


# 封装常用数据库操作
def check_user(name):
    # 注意sql中''的嵌套问题
    sql = "select * from student where name ='{}'".format ( name )
    result = query_db ( sql )
    return True if result else False


def add_user(no, name, sex, age) :
    sql = "insert into student (no,name,sex,age) values ('{}','{}','{}','{}')".format ( no, name, sex, age )
    change_db ( sql )


def del_user(name):
    sql = "delete from student where name = '{}'".format ( name )
    change_db ( sql )


