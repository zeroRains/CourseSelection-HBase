# 从app模块中即从__init__.py中导入创建的app应用
import traceback
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


@app.route('/stu/stuRegister/sno=<sno>&name=<name>&passwd=<passwd>', methods=['POST'])
def stuRegister(sno, name, passwd):
    m = md5()
    userid = None
    if not isinstance(sno, str):
        sno = str(sno)
    if not isinstance(passwd, str):
        passwd = str(passwd)
    if not isinstance(name, str):
        name = str(name)
    try:
        conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                                password="PommesPeter@123", host="10.0.0.3", port="15432")
        cursor = conn.cursor()
        userid = uuid.uuid3(uuid.NAMESPACE_DNS, sno)  # 用uuid生成userid
        m.update(passwd.encode("utf-8"))  # md5加密密码
        encrypt_passwd = m.hexdigest()
        cursor.execute(
            f"insert into test.student(sno, name, passwd, userid) values('{sno}', '{name}', '{encrypt_passwd}', '{userid}')")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        traceback.print_exc()
        return {"status": "failure", "data": []}
    return {"status": "success", "data": str(userid)}


@app.route('/stu/stuLogin/sno=<sno>&passwd=<passwd>', methods=['POST'])
def stuLogin(sno, passwd):
    m = md5()
    userid = None
    db_passwd = None
    if not isinstance(sno, str):
        sno = str(sno)
    if not isinstance(passwd, str):
        passwd = str(passwd)
    try:
        conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                                password="PommesPeter@123", host="10.0.0.3", port="15432")
        cursor = conn.cursor()
        cursor.execute(f"select passwd, userid from test.student where sno={sno}")
        rows = cursor.fetchall()
        for row in rows:
            db_passwd = row[0]
            userid = row[1]
        cursor.close()
        conn.close()

        m.update(passwd.encode("utf-8"))  # md5加密密码
        md_passwd = m.hexdigest()
        print(db_passwd, md_passwd)
        if db_passwd == md_passwd:
            return {"status": "success", "data": str(userid)}
        else:
            return {"status": "failure", "data": []}
    except Exception as e:
        traceback.print_exc()
        return {"status": "error", "data": []}


@app.route('/teacher/teacherRegister/work_no=<work_no>&name=<name>&passwd=<passwd>', methods=['POST'])
def teacherRegister(work_no, name, passwd):
    m = md5()
    if not isinstance(work_no, str):
        work_no = str(work_no)
    if not isinstance(passwd, str):
        passwd = str(passwd)
    if not isinstance(name, str):
        name = str(name)
    try:
        conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                                password="PommesPeter@123", host="10.0.0.3", port="15432")
        cursor = conn.cursor()
        userid = uuid.uuid3(uuid.NAMESPACE_DNS, work_no)  # 用uuid生成userid
        m.update(passwd.encode("utf-8"))  # md5加密密码
        encrypt_passwd = m.hexdigest()
        cursor.execute(
            f"insert into test.teacher(work_no, name, passwd, userid) values('{work_no}', '{name}', '{encrypt_passwd}', '{userid}')")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        traceback.print_exc()
        return {"status": "failure", "data": []}
    return {"status": "success", "data": str(userid)}


@app.route("/teacher/teacherRegister/work_no=<work_no>&passwd=<passwd>")
def teacherLogin(work_no, passwd):
    m = md5()
    userid = None
    db_passwd = None
    if not isinstance(work_no, str):
        work_no = str(work_no)
    if not isinstance(passwd, str):
        passwd = str(passwd)
    try:
        conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                                password="PommesPeter@123", host="10.0.0.3", port="15432")
        cursor = conn.cursor()
        cursor.execute(f"select passwd, userid from test.teacher where work_no={work_no}")
        rows = cursor.fetchall()
        for row in rows:
            db_passwd = row[0]
            userid = row[1]
        cursor.close()
        conn.close()
        m.update(passwd.encode("utf-8"))
        md_passwd = m.hexdigest()
        if db_passwd == md_passwd:
            return {"status": "failure", "data": userid}
        else:
            return {"status": "failure", "data": []}
    except Exception as e:
        traceback.print_exc()
        return {"status": "error", "data": []}


@app.route("/stu/getStuInfo/userid=<userid>", methods=['POST'])
def getStuInfo(userid):
    stu_info_list = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(f"select * from test.student where userid='{userid}'")
    rows = cursor.fetchall()
    if len(rows):
        for row in rows:
            stu_info_list.append(
                {"sno": row[1], "sex": row[2], "age": row[3], "birthday": row[4], "name": row[5], "userid": row[6]})
    else:
        cursor.close()
        conn.close()
        return {"status": "failure", "data": []}
    cursor.close()
    conn.close()
    return {"status": "success", "data": stu_info_list}


@app.route("/stu/getStuDept")
def getStuDept():
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")


@app.route("/stu/updateStuInfo/info=<info>")
def updateStuInfo(info):
    # userid name sex age birthday
    info_list = info.split(",")
    conn = psycopg2.connect(database="postgres", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"update student set name={info_list[1]}, sex={info_list[2]}, age={info_list[3]}, birthday={info_list[4]} where sno={info_list[0]}")
    cursor.commit()
    cursor.close()
    conn.close()
    return {"status": "success", "data": []}


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
