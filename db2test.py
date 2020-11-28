from db2 import DB

db=DB()

if db.check_user("张三"):
    db.del_user("张三")