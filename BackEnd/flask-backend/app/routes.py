# 从app模块中即从__init__.py中导入创建的app应用
import uuid
from hashlib import md5

import psycopg2
from flask import render_template

from app import app


# 建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@app.route('/')
def index():
    return "Hello,World!!!!"


@app.route('/error')
def error_page():
    return render_template('404.html')


@app.route('/stu/stuRegister')
def stuRegister(username, birthday):
    if not isinstance(username, str):
        username = str(username)
    if not isinstance(birthday, str):
        passwd = str(birthday)
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    # process user info
    userid = uuid.uuid3(uuid.NAMESPACE_DNS, username)
    encrypt_passwd = md5(passwd)
    cursor.execute(f"INSERT INTO student(sno, passwd, userid) values({username}, {encrypt_passwd}, {userid})")
    conn.commit()
    cursor.close()
    conn.close()
    return userid


@app.route('/st/test/name=<name>&www=<www>', methods=['POST'])
def test(name, www):
    print(name, www)
    return str(name) + str(www)


@app.route('/stu/stuLogin/sno=<sno>&passwd=<passwd>', methods=['POST'])
def stuLogin(sno, passwd):
    userid = None
    db_passwd = None
    if not isinstance(sno, str):
        sno = str(sno)
    if not isinstance(passwd, str):
        passwd = str(passwd)
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    # process user info
    cursor.execute(f"select passwd, userid from student where sno={sno}")
    rows = cursor.fetchall()
    for row in rows:
        db_passwd = row[0]
        userid = row[1]
    cursor.close()
    conn.close()
    if db_passwd == passwd:
        return userid
    else:
        return "failure"


@app.route('/teacher/teacherLogin')
def teacherLogin(username, passwd):
    if not isinstance(username, str):
        username = str(username)
    if not isinstance(passwd, str):
        passwd = str(passwd)
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    # process user info
    userid = uuid.uuid3(uuid.NAMESPACE_DNS, username)
    encrypt_passwd = md5(passwd)
    cursor.execute(f"INSERT INTO teacher(workno, passwd, userid) values({username}, {encrypt_passwd}, {userid})")
    conn.commit()
    cursor.close()
    conn.close()
    return userid


@app.route("/stu/getStuInfo")
def getStuInfo(sno):
    stu_info_list = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(f"select * from student where sno={sno}")
    rows = cursor.fetchall()
    for row in rows:
        stu_info_list.append(
            {"sno": row[1], "sex": row[2], "age": row[3], "birthday": row[4], "name": row[5], "userid": row[6]})
    cursor.close()
    conn.close()
    return str(stu_info_list)


@app.route("/stu/getStuDept")
def getStuDept():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")


@app.route("/stu/updateStuInfo")
def updateStuInfo(info: dict):
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"update student set sex={info['sex']}, age={info['age']}, birthday={info['birthday']} where sno={info['sno']}")
    cursor.commit()
    cursor.close()
    conn.close()
    return "success"


@app.route("/stu/getStuScore")
def getStuScore():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")


@app.route("/stu/getStuTable")
def getStuTable():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/stu/addStuTable")
def addStuTable():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/getTeacherInfo")
def getTeacherInfo(workno):
    teacher_info_list = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(f"select * from teacher where workno={workno}")
    rows = cursor.fetchall()
    for row in rows:
        teacher_info_list.append(
            {"sno": row[1], "sex": row[2], "age": row[3], "birthday": row[4], "name": row[5], "userid": row[6]})
    cursor.close()
    conn.close()
    return str(teacher_info_list)


@app.route("/teacher/updateTeacherInfo")
def updateTeacherInfo(info: dict):
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"update teacher set sex={info['sex']}, age={info['age']}, birthday={info['birthday']} where sno={info['sno']}")
    cursor.commit()
    cursor.close()
    conn.close()
    return "success"


@app.route("/teacher/addStuScore")
def addStuScore():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/addStuScoreWithFile")
def addStuScoreWithFile():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/getStuScores")
def getStuScores():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/delCourseScheduleTable")
def delCourseScheduleTable():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/delCourse")
def delCourse():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/addNewCourseSchedule")
def addNewCourseSchedule():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/getCourseScheduleTable")
def getCourseScheduleTable():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/addNewCourse")
def addNewCourse():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route("/teacher/getCourseTable")
def getCourseTable():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass
