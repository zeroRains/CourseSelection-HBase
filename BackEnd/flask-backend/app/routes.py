# 从app模块中即从__init__.py中导入创建的app应用
import os
import traceback

import happybase
import pandas as pd
from flask import render_template, request

from app import app
from utils.config import config_dict
from utils.ReadTable import LoadData


# 建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@app.route('/')
def index():
    return "Hello,World!!!!"


@app.route('/error')
def error_page():
    return render_template('404.html')


# ---- 学生端接口 ----
#
# @app.route('/stu/stuRegister/sno=<sno>&name=<name>&passwd=<passwd>', methods=['GET', 'POST'])
# def stuRegister(sno, name, passwd):
#     """
#     学生注册接口
#     :param sno:
#     :param name:
#     :param passwd:
#     :return:
#     """
#     m = md5()
#     if not isinstance(sno, str):
#         sno = str(sno)
#     if not isinstance(passwd, str):
#         passwd = str(passwd)
#     if not isinstance(name, str):
#         name = str(name)
#     try:
#         conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                                 password="PommesPeter@123", host="10.0.0.3", port="15432")
#         cursor = conn.cursor()
#         userid = uuid.uuid3(uuid.NAMESPACE_DNS, sno)  # 用uuid生成userid
#         m.update(passwd.encode("utf-8"))  # md5加密密码
#         encrypt_passwd = m.hexdigest()
#         cursor.execute(
#             f"insert into student(sno, name, passwd, userid) values('{sno}', '{name}', '{encrypt_passwd}', '{userid}')")
#         conn.commit()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         traceback.print_exc()
#         return {"status": "failure", "data": []}
#     return {"status": "success", "data": str(userid)}


@app.route('/stu/stuLogin/sno=<sno>&passwd=<passwd>', methods=['GET', 'POST'])
def stuLogin(sno, passwd):
    """
    学生登录接口
    :param sno:
    :param passwd:
    :return:
    """
    # test：
    # http://111.229.52.254:9779/stu/stuLogin/sno=1900300101&passwd=123456
    # m = md5()
    conn = happybase.Connection("127.0.0.1", 9090)
    table = conn.table(config_dict["table"]["student"])
    data = table.row(str(sno))
    # m.update(passwd.encode("utf-8"))
    # md_passwd = m.hexdigest()
    md_passwd = passwd
    bd_password = data[bytes(config_dict['name']['密码'], "ascii")]
    conn.close()
    if md_passwd == str(bd_password, 'utf-8'):
        return {"status": "success", "data": str(sno)}
    else:
        return {"status": "failure", "data": []}


#
# @app.route('/teacher/teacherRegister/tno=<tno>&name=<name>&passwd=<passwd>', methods=['POST'])
# def teacherRegister(tno, name, passwd):
#     """
#     教师账号注册
#     :param tno:
#     :param name:
#     :param passwd:
#     :return:
#     """
#     m = md5()
#     if not isinstance(tno, str):
#         tno = str(tno)
#     if not isinstance(passwd, str):
#         passwd = str(passwd)
#     if not isinstance(name, str):
#         name = str(name)
#     try:
#         conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                                 password="PommesPeter@123", host="10.0.0.3", port="15432")
#         cursor = conn.cursor()
#         userid = uuid.uuid3(uuid.NAMESPACE_DNS, tno)  # 用uuid生成userid
#         m.update(passwd.encode("utf-8"))  # md5加密密码
#         encrypt_passwd = m.hexdigest()
#         cursor.execute(
#             f"insert into teacher(tno, name, passwd, userid) values('{tno}', '{name}', '{encrypt_passwd}', '{userid}')")
#         conn.commit()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         traceback.print_exc()
#         return {"status": "failure", "data": []}
#     return {"status": "success", "data": str(userid)}

#
# @app.route("/teacher/teacherLogin/tno=<tno>&passwd=<passwd>", methods=["POST"])
# def teacherLogin(tno, passwd):
#     """
#     教师登录接口
#     :param tno:
#     :param passwd:
#     :return:
#     """
#     m = md5()
#     userid = None
#     db_passwd = None
#     if not isinstance(tno, str):
#         tno = str(tno)
#     if not isinstance(passwd, str):
#         passwd = str(passwd)
#     try:
#         conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                                 password="PommesPeter@123", host="10.0.0.3", port="15432")
#         cursor = conn.cursor()
#         cursor.execute(f"select passwd, userid from teacher where tno={tno}")
#         rows = cursor.fetchall()
#         for row in rows:
#             db_passwd = row[0]
#             userid = row[1]
#         cursor.close()
#         conn.close()
#         m.update(passwd.encode("utf-8"))
#         md_passwd = m.hexdigest()
#         if db_passwd == md_passwd:
#             return {"status": "success", "data": userid}
#         else:
#             return {"status": "failure", "data": []}
#     except Exception as e:
#         traceback.print_exc()
#         return {"status": "error", "data": []}
#

@app.route("/stu/getStuInfo/userid=<userid>", methods=['GET'])
def getStuInfo(userid):
    """
    获取学生信息
    :param userid:
    :return:
    """
    # test
    # http://111.229.52.254:9779/stu/getStuInfo/userid=1900300101
    conn = happybase.Connection("127.0.0.1", 9090)
    table = conn.table(config_dict["table"]["student"])
    data = table.row(str(userid))
    datas = []
    conn.close()
    if data is not None:
        data_dir = {"sno": str(data[bytes(config_dict["name"]["学号"], 'ascii')], 'utf-8'),
                    "name": str(data[bytes(config_dict["name"]["姓名"], 'ascii')], 'utf-8'),
                    "sex": str(data[bytes(config_dict["name"]["性别"], 'ascii')], 'utf-8'),
                    "age": str(data[bytes(config_dict["name"]["年龄"], 'ascii')], 'utf-8'),
                    "department": str(data[bytes(config_dict["name"]["学院"], 'ascii')], 'utf-8'),
                    "major": str(data[bytes(config_dict["name"]["专业"], 'ascii')], 'utf-8')
                    }
        datas.append(data_dir)
        conn.close()
        return {"status": "success", "data": datas}
    else:
        conn.close()
        return {"status": "failure", "data": datas}


@app.route("/stu/getStuScore/userid=<userid>", methods=["GET"])
def getStuScore(userid):
    """
    获得某个学生的所有课程成绩
    :param userid:
    :return:
    """
    conn = happybase.Connection("127.0.0.1", 9090)
    table = conn.table(config_dict["table"]["record"])
    courses = conn.table(config_dict["table"]["course"])
    score_info = []
    fill = f"SingleColumnValueFilter ('studentid', 'studentid', =, 'binary:{userid}')"
    iters = table.scan(filter=fill)
    if iters is None:
        return {"status": "failure", "data": score_info}
    for row, val in iters:
        course = courses.row(
            str(val[bytes(config_dict["name"]["课程课号"], "ascii")], "utf-8"))
        score = str(val[bytes(config_dict["name"]["分数"], 'ascii')], 'utf-8')
        score_info.append({"name": str(course[bytes(config_dict["name"]["名称"], 'ascii')], 'utf-8'),
                           "credit": str(course[bytes(config_dict["name"]["学分"], 'ascii')], 'utf-8'),
                           "score": score if score != '-1' else "未考试",
                           "coursecode": str(course[bytes(config_dict["name"]["课号"], 'ascii')], 'utf-8'),
                           })
    conn.close()
    return {"status": "success", "data": score_info}


@app.route("/stu/getCoureseTable/userid=<userid>", methods=["GET"])
def getCourseTable_stu(userid):
    """
    获取学生的已选课程
    :param userid:
    :return:
    """
    # http://111.229.52.254:9779/stu/getCoureseTable/userid=1900300101
    conn = happybase.Connection("127.0.0.1", 9090)
    record = conn.table(config_dict["table"]["record"])
    courses = conn.table(config_dict["table"]["course"])
    res_data = []
    fill = f"SingleColumnValueFilter ('studentid', 'studentid', =, 'binary:{userid}')"
    iters = record.scan(filter=fill)
    if iters is None:
        return {"status": "No data", "data": []}
    for key, val in iters:
        course = courses.row(
            str(val[bytes(config_dict["name"]["课程课号"], "ascii")], 'utf-8'))
        res_data.append({"name": str(course[bytes(config_dict["name"]["名称"], 'ascii')], 'utf-8'),
                         "coursecode": str(course[bytes(config_dict["name"]["课号"], 'ascii')], 'utf-8'),
                         "credit": str(course[bytes(config_dict["name"]["学分"], 'ascii')], 'utf-8'),
                         })
    conn.close()
    return {"status": "success", "data": res_data}


@app.route("/stu/addStuCourse/userid=<userid>&cno=<cno>")
def addStuCourse(userid, cno):
    """
    选课接口
    :return:
    """
    # http://111.229.52.254:9779/stu/addStuCourse/userid=1900300101&cno=2020199
    conn = happybase.Connection("127.0.0.1", 9090)
    record = conn.table(config_dict["table"]["record"])
    row = f"{cno}-{userid}"
    try:
        record.put(row, {config_dict["name"]["课程课号"]: str(cno),
                         config_dict["name"]["学生学号"]: str(userid),
                         config_dict["name"]["分数"]: str(-1)})
        conn.close()
        return {"status": "success", "data": []}
    except Exception as e:
        print(e)
        conn.close()
        return {"status": "failure", "data": []}


@app.route("/stu/isChoosible/coursecode=<coursecode>", methods=["GET"])
def is_Choosible(coursecode):
    conn = happybase.Connection("127.0.0.1", 9090)
    record = conn.table(config_dict["table"]["record"])
    course = conn.table(config_dict["table"]["course"])

    # choosible_class_list = []
    # conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
    #                         password="PommesPeter@123", host="10.0.0.3", port="15432")
    # cursor = conn.cursor()
    # try:
    #     cursor.execute(
    #         f"select schedule.cno, semester, day, index, classroom, optional, selected, startweek, endweek, teach.tno, teacher.name, course.name  from schedule join course on course.coursecode=schedule.coursecode join teach on teach.cno=schedule.cno join teacher on teach.tno=teacher.tno where schedule.coursecode='{coursecode}'")
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         cursor.execute(
    #             f"select day, index from schedule join selection on selection.cno=schedule.cno where day={row[2]} and index={row[3]}")
    #         course_rows = cursor.fetchall()
    #         if not len(course_rows):
    #             choosible_class_list.append(
    #                 {"cno": row[0], "semester": row[1], "day": row[2], "index": row[3], "classroom": row[4],
    #                  "optional": row[5], "selected": row[6], "startweek": row[7], "endweek": row[8], "tno": row[9],
    #                  "tname": row[10], "cname": row[11]})
    #         else:
    #             cursor.execute(
    #                 f"select startweek, endweek from schedule join selection on selection.cno=schedule.cno where day={row[2]} and index={row[3]}")
    #             time_rows = cursor.fetchall()
    #             for item in time_rows:
    #                 if int(row[7]) > item[1] or int(row[8]) < item[0]:
    #                     choosible_class_list.append(
    #                         {"cno": row[0], "semester": row[1], "day": row[2], "index": row[3], "classroom": row[4],
    #                          "optional": row[5], "selected": row[6], "startweek": row[7], "endweek": row[8],
    #                          "tno": row[9],
    #                          "tname": row[10], "cname": row[11]})
    #     cursor.close()
    #     conn.close()
    #     return {"status": "success", "data": choosible_class_list}
    # except Exception as e:
    #     traceback.print_exc()
    #     return {"status": "failure", "data": []}
    pass


@app.route("/stu/selectCourse/userid=<userid>", methods=["GET"])
def selectCourse(userid):
    """
    学生可以选择的课程列表
    :param userid:
    :return:
    """
    conn = happybase.Connection("127.0.0.1", 9090)
    record = conn.table(config_dict["table"]["record"])
    course = conn.table(config_dict["table"]["course"])
    selected_course = []
    res_data = []
    fill = f"SingleColumnValueFilter ('studentid', 'studentid', =, 'binary:{userid}')"
    iters = record.scan(filter=fill)
    if iters is not None:
        for key, val in iters:
            selected_course.append(
                str(val[bytes(config_dict["name"]["课程课号"], 'ascii')], 'utf-8'))
        selected_course = set(selected_course)
    iters = course.scan()
    # conn.close()
    if iters is None:
        return {"status": "success", "data": []}
    else:
        for key, val in iters:
            if str(key, "utf-8") not in selected_course:
                res_data.append({"coursecode": str(key, 'utf-8'),
                                 "name": str(val[bytes(config_dict["name"]["名称"], 'ascii')], "utf-8"),
                                 "credit": str(val[bytes(config_dict["name"]["学分"], 'ascii')], "utf-8"),
                                 "time": str(val[bytes(config_dict["name"]["学年"], 'ascii')], "utf-8"),
                                 "teacher": str(val[bytes(config_dict["name"]["老师"], 'ascii')], "utf-8"), })
        conn.close()
        return {"status": "success", "data": res_data}


@app.route("/stu/delStuCourse/userid=<userid>&cno=<cno>", methods=["POST"])
def delStuCourse(userid, cno):
    """
    这个是用于点击退课按钮的接口
    :param userid:
    :param cno:
    :return:
    """
    conn = happybase.Connection("127.0.0.1", 9090)
    record = conn.table(config_dict["table"]["record"])
    try:
        record.delete(f"{cno}-{userid}")
        conn.close()
        return {"status": "success", "data": []}
    except Exception as e:
        print(e)
        conn.close()
        return {"status": "failure", "data": []}


@app.route("/stu/deleteCourseList/userid=<userid>", methods=["GET"])
def getNotSelectedCourse_stu(userid):
    """
    学生可以退课的接口
    :param userid:
    :return:
    """
    conn = happybase.Connection("127.0.0.1", 9090)
    record = conn.table(config_dict["table"]["record"])
    course = conn.table(config_dict["table"]["course"])
    fill = f"SingleColumnValueFilter ('studentid', 'studentid', =, 'binary:{userid}')"
    fill1 = f"SingleColumnValueFilter ('score', 'score', =, 'binary:{str(-1)}')"
    iters = record.scan(filter=f"{fill} AND {fill1}")
    res = []
    courses = []
    if iters is None:
        return {"status": "success", "data": []}
    else:
        for key, val in iters:
            courses.append(
                str(val[bytes(config_dict["name"]["课程课号"], "ascii")], "utf-8"))
        iters = course.scan()
        for key, val in iters:
            if str(key, 'utf-8') in courses:
                res.append({
                    "coursecode": str(val[bytes(config_dict["name"]["课号"], "ascii")], "utf-8"),
                    "name": str(val[bytes(config_dict["name"]["名称"], "ascii")], "utf-8"),
                    "credit": str(val[bytes(config_dict["name"]["学分"], "ascii")], "utf-8"),
                })
        conn.close()
        return {"status": "success", "data": res}


#
# # ---- 老师端接口 ----
#
# @app.route("/teacher/getTeacherInfo/userid=<userid>", methods=['POST'])
# def getTeacherInfo(userid):
#     """
#     获取老师信息
#     :param userid:
#     :return:
#     """
#     teacher_info_list = []
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     try:
#         cursor.execute(
#             f"select tno, teacher.name, sex, birthday, age, position, college.name from teacher join college on teacher.collegenum=college.num where userid='{userid}'")
#         rows = cursor.fetchall()
#         if len(rows):
#             for row in rows:
#                 teacher_info_list.append(
#                     {"tno": row[0], "tname": row[1], "sex": row[2], "birthday": row[3], "age": row[4],
#                      "position": row[5],
#                      "college_name": row[6]})
#         else:
#             cursor.close()
#             conn.close()
#             return {"status": "failure", "data": []}
#         cursor.close()
#         conn.close()
#         return {"status": "success", "data": teacher_info_list}
#     except Exception as e:
#         traceback.print_exc()
#         return {"status": "failure", "data": []}

#
# @app.route("/teacher/updateTeacherInfo/userid=<userid>&info=<info>", methods=["POST"])
# def updateTeacherInfo(userid, info):
#     """
#     更新教师信息
#     :param userid:
#     :param info:
#     :return:
#     """
#     # userid name sex age birthday college_name
#     info_list = info.split(",")
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     try:
#         cursor.execute(
#             f"update teacher set name='{info_list[0]}', sex='{info_list[1]}', age='{info_list[2]}', birthday='{info_list[3]}', position='{info_list[4]}' where userid='{userid}'")
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return {"status": "success", "data": []}
#     except Exception as e:
#         cursor.close()
#         conn.close()
#         traceback.print_exc()
#         return {"status": "failure", "data": []}
#
#
# @app.route("/teacher/addStuScore/cno=<cno>&sno=<sno>&usual=<usual>&exam=<exam>&score=<score>")
# def addStuScore(cno, sno, usual, exam, score):
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     try:
#         cursor.execute(f"update selection set usual={usual}, exam={exam}, score={score} where cno={cno} and sno={sno}")
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return {"status": "success", "data": []}
#     except Exception as e:
#         traceback.print_exc()
#         cursor.close()
#         conn.close()
#         return {"status": "failure", "data": []}
#
#
# @app.route("/teacher/addStuScoreWithFile")
# def addStuScoreWithFile():
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     if request.method == 'POST':
#         f = request.files['file']


@app.route("/stu/getStuScores/userid=<userid>", methods=["GET"])
def getStuScores_stu(userid):
    """
    学生查询自己的成绩
    :param userid:upd
    :return:
    """
    # score_info = []
    # conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
    #                         password="PommesPeter@123", host="10.0.0.3", port="15432")
    # cursor = conn.cursor()
    # cursor.execute(
    #     f"select cno, usual, exam, score from student join selection on student.sno=selection.sno where userid='{userid}'")
    # rows = cursor.fetchall()
    # if len(rows):
    #     for row in rows:
    #         score_info.append(
    #             {"cno": row[0], "usual": row[1], "exam": row[2], "score": row[3]})
    # else:
    #     cursor.close()
    #     conn.close()
    #     return {"status": "No data", "data": []}
    # cursor.close()
    # conn.close()
    # return {"status": "success", "data": score_info}
    pass


#
# @app.route("/teacher/getStuScores/userid=<userid>", methods=["GET"])
# def getStuScores_teacher(userid):
#     """
#     老师获取自己所教的课的成绩
#     :param userid:
#     :return:
#     """
#     score_info = []
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     try:
#         cursor.execute(f"select * from student where userid='{userid}'")
#         rows = cursor.fetchall()
#         if len(rows):
#             for row in rows:
#                 score_info.append(
#                     {"sno": row[1], "sex": row[2], "age": row[3], "birthday": row[4], "name": row[5], "userid": row[6]})
#         else:
#             cursor.close()
#             conn.close()
#             return {"status": "No data", "data": []}
#         cursor.close()
#         conn.close()
#         return {"status": "success", "data": score_info}
#     except Exception as e:
#         traceback.print_exc()
#         return {"status": "failure", "data": []}
#
#
# @app.route("/teacher/delCourseScheduleTable/cno=<cno>")
# def delCourseScheduleTable(cno):
#     """
#     删除课程计划
#     :return:
#     """
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     try:
#
#         cursor.execute(f"delete from schedule where cno={cno}")
#     except Exception as e:
#         traceback.print_exc()
#         return {"status": "failure", "data": []}
#     conn.commit()
#     return {"status": "success", "data": []}
#
#
# @app.route("/teacher/delCourse")
# def delCourse():
#     """
#     删除课程
#     :return:
#     """
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     pass
#
#
# @app.route(
#     "/teacher/addNewCourseSchedule/userid=<userid>&cno=<cno>&coursecode=<coursecode>&semester=<semester>&classroom=<classroom>&time=<time>&optional=<optional>",
#     methods=["POST"])
# def addNewCourseSchedule(userid, cno, coursecode, semester, classroom, time, optional):
#     """
#     添加新的课程计划
#     :param userid:
#     :param cno:
#     :param coursecode:
#     :param semester:
#     :param classroom:
#     :param time: 星期，节次，开始周，结束周
#     :param selected:
#     :return:
#     """
#     # time: 星期，节次，开始周，结束周
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     time_list = time.split(",")
#     day = time_list[0]
#     index = time_list[1]
#     startweek = time_list[2]
#     endweek = time_list[3]
#     cursor = conn.cursor()
#     try:
#         cursor.execute(
#             f"select day, index from schedule join teach on teach.cno=schedule.cno where day={day} and index={index}")
#         rows = cursor.fetchall()
#         if not len(rows):
#             print("case:1")
#             cursor.execute(
#                 f"insert into schedule(cno, semester, day, index, classroom, optional, selected, startweek, endweek, coursecode) values ('{cno}', '{semester}', '{day}', '{index}', '{classroom}', '{optional}', 0, '{startweek}', '{endweek}', '{coursecode}')")
#             cursor.execute(f"select tno from teacher where userid='{userid}'")
#             tno = cursor.fetchall()
#             cursor.execute(f"select tno from teach where tno='{tno[0][0]}' and cno='{cno}'")
#             is_exists_tno = cursor.fetchall()
#             if not len(is_exists_tno):
#                 cursor.execute(f"insert into teach(tno, cno) values ('{tno[0][0]}', '{cno}')")
#                 conn.commit()
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return {"status": "success", "data": []}
#         else:
#             print("case:2")
#             cursor.execute(f"select startweek, endweek from schedule where day={day} and index={index}")
#             time_rows = cursor.fetchall()
#             for row in time_rows:
#                 if int(startweek) > row[1] or int(endweek) < row[0]:
#                     cursor.execute(
#                         f"insert into schedule(cno, semester, day, index, classroom, optional, selected, startweek, endweek, coursecode) values ('{cno}', '{semester}', '{day}', '{index}', '{classroom}', {optional}, 0, '{startweek}', '{endweek}', '{coursecode}')")
#                     conn.commit()
#                     cursor.execute(f"select tno from teacher where userid='{userid}'")
#                     tno = cursor.fetchall()
#                     cursor.execute(f"select tno from teach where tno='{tno[0][0]}' and cno='{cno}'")
#                     is_exists_tno = cursor.fetchall()
#                     if not len(is_exists_tno):
#                         cursor.execute(f"insert into teach(tno, cno) values ('{tno[0][0]}', '{cno}')")
#                         conn.commit()
#                 else:
#                     cursor.close()
#                     conn.close()
#                     return {"status": "failure", "data": []}
#                 conn.commit()
#             cursor.close()
#             conn.close()
#             return {"status": "success", "data": []}
#     except Exception as e:
#         traceback.print_exc()
#         return {"status": "failure", "data": [str(e.with_traceback(traceback.print_exc()))]}
#
#
# @app.route("/teacher/addNewCourse/coursecode=<coursecode>&name=<name>&credit=<credit>", methods=["POST"])
# def addNewCourse(coursecode, name, credit):
#     """
#     添加新的课程
#     :param coursecode:
#     :param name:
#     :param credit:
#     :return:
#     """
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     try:
#         cursor.execute(f"insert into course(coursecode, name, credit) values ('{coursecode}', '{name}', '{credit}')")
#         conn.commit()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         traceback.print_exc()
#         cursor.close()
#         conn.close()
#         return {"status": "failure", "data": [str(e.with_traceback(traceback.print_exc()))]}
#     return {"status": "success", "data": []}
#
#
# @app.route("/teacher/getTeachTable/userid=<userid>", methods=["GET"])
# def getTeachTable(userid):
#     """
#     获取特定老师所教的课
#     :param userid:
#     :return:
#     """
#     teachTable_info = []
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     cursor.execute(
#         f"select teacher.name, teach.cno, course.credit, course.name, schedule.selected, schedule.optional from teach join teacher on teacher.tno=teach.tno join schedule on schedule.cno=teach.cno join course on course.coursecode=schedule.coursecode where teacher.userid='{userid}'")
#     rows = cursor.fetchall()
#     for row in rows:
#         teachTable_info.append(
#             {"tname": row[0], "cno": row[1], "cname": row[2], "credit": row[3], "selected": row[4], "optional": row[5]})
#     cursor.close()
#     conn.close()
#     return {"status": "success", "data": teachTable_info}
#
#
# @app.route("/teacher/getCourseScheduleTable/userid=<userid>", methods=["GET"])
# def getCourseScheduleTable_teacher(userid):
#     """
#     获取老师自己的课程计划
#     :param userid:
#     :return:
#     """
#     schedule_list = []
#     conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
#                             password="PommesPeter@123", host="10.0.0.3", port="15432")
#     cursor = conn.cursor()
#     cursor.execute(
#         f"select schedule.cno, schedule.coursecode, course.name, schedule.startweek, schedule.endweek, schedule.day, schedule.index, course.credit, schedule.classroom, schedule.optional, schedule.selected from schedule join course on schedule.coursecode = course.coursecode where schedule.cno in (select cno from teach join teacher on teach.tno = teacher.tno where teacher.userid='{userid}')")
#     rows = cursor.fetchall()
#     if len(rows):
#         for row in rows:
#             schedule_list.append(
#                 {"cno": row[0], "coursecode": row[1], "cname": row[2], "startweek": row[3], "endweek": row[4],
#                  "day": row[5], "index": row[6], "credit": row[7], "classroom": row[8], "optional": row[9],
#                  "selected": row[10]})
#         cursor.close()
#         conn.close()
#         return {"status": "success", "data": schedule_list}
#     else:
#         cursor.close()
#         conn.close()
#         return {"status": "No data", "data": schedule_list}


# ---- 通用接口 ----

@app.route("/all/getAllCourse", methods=["GET"])
def getCourseTable_all():
    """
    获取全部的课程信息
    :return:
    """
    conn = happybase.Connection("127.0.0.1", 9090)
    course = conn.table(config_dict["table"]["course"])
    iters = course.scan()
    res = []
    for key, val in iters:
        res.append({
            "cno": str(val[bytes(config_dict["name"]["课号"], "ascii")], 'utf-8'),
            "cname": str(val[bytes(config_dict["name"]["名称"], "ascii")], 'utf-8'),
            "credit": str(val[bytes(config_dict["name"]["学分"], "ascii")], 'utf-8'),
            "semester": str(val[bytes(config_dict["name"]["学年"], "ascii")], 'utf-8'),
            "teacher": str(val[bytes(config_dict["name"]["老师"], "ascii")], 'utf-8'),
            "grade": str(val[bytes(config_dict["name"]["职称"], "ascii")], 'utf-8'),
        })
    conn.close()
    return {"status": "success", "data": res}


@app.route("/all/getAllStudent", methods=["GET"])
def getCourseScheduleTable():
    """
    获得所有的学生信息
    :return:
    """
    conn = happybase.Connection("127.0.0.1", 9090)
    student = conn.table(config_dict["table"]["student"])
    res = []
    for key, val in student.scan():
        res.append({
            "sno": str(val[bytes(config_dict["name"]["学号"], 'ascii')], 'utf-8'),
            "sname": str(val[bytes(config_dict["name"]["姓名"], 'ascii')], 'utf-8'),
            "sex": str(val[bytes(config_dict["name"]["性别"], 'ascii')], 'utf-8'),
            "age": str(val[bytes(config_dict["name"]["年龄"], 'ascii')], 'utf-8'),
            "department": str(val[bytes(config_dict["name"]["学院"], 'ascii')], 'utf-8'),
            "major": str(val[bytes(config_dict["name"]["专业"], 'ascii')], 'utf-8'),
        })
    conn.close()
    return {"status": "success", "data": res}


file_save_path = "/home/hadoop/CourseSelection-HBase/BackEnd/flask-backend/static/"


@app.route("/all/upload_file/info_type=<_type>", methods=["POST"])
def upload_file(_type):
    conn = happybase.Connection("127.0.0.1", 9090)
    os.makedirs(file_save_path, exist_ok=True)
    try:
        file = request.files["file"]
        print(file, request.files, "==="*10)
        file_path = os.path.join(file_save_path, file.filename)
        file.save(file_path)
        df = pd.read_csv(file_path)
        ld = None
        if _type == "course":
            ld = LoadData(conn, course=df)
        elif _type == "student":
            ld = LoadData(conn, student=df)
        print(ld)
        if ld is not None:
            ld.load()
        conn.close()
        return {"status": "success", "data": []}
    except Exception as e:
        conn.close()
        e.with_traceback(traceback.print_exc())
        return {"status": "failed", "data": []}
