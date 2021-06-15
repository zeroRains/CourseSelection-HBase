# 从app模块中即从__init__.py中导入创建的app应用
from app import app
from flask import render_template

import psycopg2


# 建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@app.route('/')
@app.route('/index')
def index():
    return "Hello,World!!!!"


@app.route('/error')
def error_page():
    return render_template('404.html')


@app.route('/stu/stuLogin')
def login(name, passwd):
    userid = ""
    conn = psycopg2.connect(database="postgres", user="postgres",
                            password="postgres", host="192.168.1.200", port="5432")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_conn(id int, name text)")
    cursor.execute("INSERT INTO test_conn values(1,'haha')")
    # 提交SQL命令
    conn.commit()

    cursor.execute("select * from test_conn")

    # 获取SELECT返回的元组
    rows = cursor.fetchall()
    for row in rows:
        print('id = ', row[0], 'name = ', row[1], '\n')

    # 关闭游标
    cursor.close()

    # 关闭数据库连接
    conn.close()

    return userid


@app.route("/stu/getStuInfo")
def getStuInfo():
    pass
