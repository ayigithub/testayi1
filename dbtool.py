import pymysql


def chaxun(sql):
    # 连接数据库
    db = pymysql.connect(user = 'root',password = '123456',host = '127.0.0.1',db = 'ayi')
    # 获取游标
    cur = db.cursor()

    # 执行sql

    cur.execute(sql)

    # 执行结果
    res = cur.fetchall()
    db.close()

    return res



def commit(sql):
    db = pymysql.connect(user = 'root',password = '123456',host = '127.0.0.1',db = 'ayi')
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()
    return '修改成功'

# sql1 = 'update basic_info set age = 2 where name = "1"'
# sql2 = 'insert into basic_info values("2",18)'
# print(commit(sql1))
# print(commit(sql2))


# sql = 'select * from basic_info '
# a = chaxun(sql)
# print(a)