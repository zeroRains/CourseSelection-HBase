    except Exception as e:
        cursor.close()
        conn.close()
        traceback.print_exc()
        return {"status": "failure", "data": []}


@app.route("/stu/getCourseTable/userid=<userid>", methods=["GET"])
def getNotSelectedCourse_stu(userid):
    course_table = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"select course.coursecode, course.name, course.credit from course where course.coursecode not in (select schedule.coursecode from selection join schedule on schedule.cno=selection.cno join student on selection.sno=selection.sno where student.userid='{userid}')")
    rows = cursor.fetchall()
    if len(rows):
        for row in rows:
            course_table.append(
                {"cno": row[0], "name": row[1], "credit": row[2]})
    else:
        cursor.close()
        conn.close()
        return {"status": "failure", "data": []}
    cursor.close()
    conn.close()
    return {"status": "success", "data": course_table}


# ---- 老师端接口 ----

@app.route("/teacher/getTeacherInfo/userid=<userid>", methods=['POST'])
def getTeacherInfo(userid):
    """
    获取老师信息
    :param userid:
    :return:
    """
    teacher_info_list = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"select tno, teacher.name, sex, birthday, age, position, college.name from teacher join college on teacher.collegenum=college.num where userid='{userid}'")
        rows = cursor.fetchall()
        if len(rows):
            for row in rows:
                teacher_info_list.append(
                    {"tno": row[0], "tname": row[1], "sex": row[2], "birthday": row[3], "age": row[4],
                     "position": row[5],
                     "college_name": row[6]})
        else:
            cursor.close()
            conn.close()
            return {"status": "failure", "data": []}
        cursor.close()
        conn.close()
        return {"status": "success", "data": teacher_info_list}
    except Exception as e:
        traceback.print_exc()
        return {"status": "failure", "data": []}


@app.route("/teacher/updateTeacherInfo/userid=<userid>&info=<info>", methods=["POST"])
def updateTeacherInfo(userid, info):
    """
    更新教师信息
    :param userid:
    :param info:
    :return:
    """
    # userid name sex age birthday college_name
    info_list = info.split(",")
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"update teacher set name='{info_list[0]}', sex='{info_list[1]}', age='{info_list[2]}', birthday='{info_list[3]}', position='{info_list[4]}' where userid='{userid}'")
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "success", "data": []}
    except Exception as e:
        cursor.close()
        conn.close()
        traceback.print_exc()
        return {"status": "failure", "data": []}


@app.route("/teacher/addStuScore/cno=<cno>&sno=<sno>&usual=<usual>&exam=<exam>&score=<score>")
def addStuScore(cno, sno, usual, exam, score):
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    try:
        cursor.execute(f"update selection set usual={usual}, exam={exam}, score={score} where cno={cno} and sno={sno}")
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "success", "data": []}
    except Exception as e:
        traceback.print_exc()
        cursor.close()
        conn.close()
        return {"status": "failure", "data": []}


@app.route("/teacher/addStuScoreWithFile")
def addStuScoreWithFile():
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    if request.method == 'POST':
        f = request.files['file']


@app.route("/stu/getStuScores/userid=<userid>", methods=["GET"])
def getStuScores_stu(userid):
    """
    学生查询自己的成绩
    :param userid:upd
    :return:
    """
    score_info = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"select cno, usual, exam, score from student join selection on student.sno=selection.sno where userid='{userid}'")
    rows = cursor.fetchall()
    if len(rows):
        for row in rows:
            score_info.append(
                {"cno": row[0], "usual": row[1], "exam": row[2], "score": row[3]})
    else:
        cursor.close()
        conn.close()
        return {"status": "No data", "data": []}
    cursor.close()
    conn.close()
    return {"status": "success", "data": score_info}


@app.route("/teacher/getStuScores/userid=<userid>", methods=["GET"])
def getStuScores_teacher(userid):
    """
    老师获取自己所教的课的成绩
    :param userid:
    :return:
    """
    score_info = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    try:
        cursor.execute(f"select * from student where userid='{userid}'")
        rows = cursor.fetchall()
        if len(rows):
            for row in rows:
                score_info.append(
                    {"sno": row[1], "sex": row[2], "age": row[3], "birthday": row[4], "name": row[5], "userid": row[6]})
        else:
            cursor.close()
            conn.close()
            return {"status": "No data", "data": []}
        cursor.close()
        conn.close()
        return {"status": "success", "data": score_info}
    except Exception as e:
        traceback.print_exc()
        return {"status": "failure", "data": []}


@app.route("/teacher/delCourseScheduleTable/cno=<cno>")
def delCourseScheduleTable(cno):
    """
    删除课程计划
    :return:
    """
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    try:

        cursor.execute(f"delete from schedule where cno={cno}")
    except Exception as e:
        traceback.print_exc()
        return {"status": "failure", "data": []}
    conn.commit()
    return {"status": "success", "data": []}


@app.route("/teacher/delCourse")
def delCourse():
    """
    删除课程
    :return:
    """
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    pass


@app.route(
    "/teacher/addNewCourseSchedule/userid=<userid>&cno=<cno>&coursecode=<coursecode>&semester=<semester>&classroom=<classroom>&time=<time>&optional=<optional>",
    methods=["POST"])
def addNewCourseSchedule(userid, cno, coursecode, semester, classroom, time, optional):
    """
    添加新的课程计划
    :param userid:
    :param cno:
    :param coursecode:
    :param semester:
    :param classroom:
    :param time: 星期，节次，开始周，结束周
    :param selected:
    :return:
    """
    # time: 星期，节次，开始周，结束周
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    time_list = time.split(",")
    day = time_list[0]
    index = time_list[1]
    startweek = time_list[2]
    endweek = time_list[3]
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"select day, index from schedule join teach on teach.cno=schedule.cno where day={day} and index={index}")
        rows = cursor.fetchall()
        if not len(rows):
            print("case:1")
            cursor.execute(
                f"insert into schedule(cno, semester, day, index, classroom, optional, selected, startweek, endweek, coursecode) values ('{cno}', '{semester}', '{day}', '{index}', '{classroom}', '{optional}', 0, '{startweek}', '{endweek}', '{coursecode}')")
            cursor.execute(f"select tno from teacher where userid='{userid}'")
            tno = cursor.fetchall()
            cursor.execute(f"select tno from teach where tno='{tno[0][0]}' and cno='{cno}'")
            is_exists_tno = cursor.fetchall()
            if not len(is_exists_tno):
                cursor.execute(f"insert into teach(tno, cno) values ('{tno[0][0]}', '{cno}')")
                conn.commit()
            conn.commit()
            cursor.close()
            conn.close()
            return {"status": "success", "data": []}
        else:
            print("case:2")
            cursor.execute(f"select startweek, endweek from schedule where day={day} and index={index}")
            time_rows = cursor.fetchall()
            for row in time_rows:
                if int(startweek) > row[1] or int(endweek) < row[0]:
                    cursor.execute(
                        f"insert into schedule(cno, semester, day, index, classroom, optional, selected, startweek, endweek, coursecode) values ('{cno}', '{semester}', '{day}', '{index}', '{classroom}', {optional}, 0, '{startweek}', '{endweek}', '{coursecode}')")
                    conn.commit()
                    cursor.execute(f"select tno from teacher where userid='{userid}'")
                    tno = cursor.fetchall()
                    cursor.execute(f"select tno from teach where tno='{tno[0][0]}' and cno='{cno}'")
                    is_exists_tno = cursor.fetchall()
                    if not len(is_exists_tno):
                        cursor.execute(f"insert into teach(tno, cno) values ('{tno[0][0]}', '{cno}')")
                        conn.commit()
                else:
                    cursor.close()
                    conn.close()
                    return {"status": "failure", "data": []}
                conn.commit()
            cursor.close()
            conn.close()
            return {"status": "success", "data": []}
    except Exception as e:
        traceback.print_exc()
        return {"status": "failure", "data": [str(e.with_traceback(traceback.print_exc()))]}


@app.route("/teacher/addNewCourse/coursecode=<coursecode>&name=<name>&credit=<credit>", methods=["POST"])
def addNewCourse(coursecode, name, credit):
    """
    添加新的课程
    :param coursecode:
    :param name:
    :param credit:
    :return:
    """
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    try:
        cursor.execute(f"insert into course(coursecode, name, credit) values ('{coursecode}', '{name}', '{credit}')")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        traceback.print_exc()
        cursor.close()
        conn.close()
        return {"status": "failure", "data": [str(e.with_traceback(traceback.print_exc()))]}
    return {"status": "success", "data": []}


@app.route("/teacher/getTeachTable/userid=<userid>", methods=["GET"])
def getTeachTable(userid):
    """
    获取特定老师所教的课
    :param userid:
    :return:
    """
    teachTable_info = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"select teacher.name, teach.cno, course.credit, course.name, schedule.selected, schedule.optional from teach join teacher on teacher.tno=teach.tno join schedule on schedule.cno=teach.cno join course on course.coursecode=schedule.coursecode where teacher.userid='{userid}'")
    rows = cursor.fetchall()
    for row in rows:
        teachTable_info.append(
            {"tname": row[0], "cno": row[1], "cname": row[2], "credit": row[3], "selected": row[4], "optional": row[5]})
    cursor.close()
    conn.close()
    return {"status": "success", "data": teachTable_info}


@app.route("/teacher/getCourseScheduleTable/userid=<userid>", methods=["GET"])
def getCourseScheduleTable_teacher(userid):
    """
    获取老师自己的课程计划
    :param userid:
    :return:
    """
    schedule_list = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"select schedule.cno, schedule.coursecode, course.name, schedule.startweek, schedule.endweek, schedule.day, schedule.index, course.credit, schedule.classroom, schedule.optional, schedule.selected from schedule join course on schedule.coursecode = course.coursecode where schedule.cno in (select cno from teach join teacher on teach.tno = teacher.tno where teacher.userid='{userid}')")
    rows = cursor.fetchall()
    if len(rows):
        for row in rows:
            schedule_list.append(
                {"cno": row[0], "coursecode": row[1], "cname": row[2], "startweek": row[3], "endweek": row[4],
                 "day": row[5], "index": row[6], "credit": row[7], "classroom": row[8], "optional": row[9],
                 "selected": row[10]})
        cursor.close()
        conn.close()
        return {"status": "success", "data": schedule_list}
    else:
        cursor.close()
        conn.close()
        return {"status": "No data", "data": schedule_list}


# ---- 通用接口 ----

@app.route("/all/getCourseTable", methods=["GET"])
def getCourseTable_all():
    course_table = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"select course.coursecode, course.name, course.credit from course")
    rows = cursor.fetchall()
    if len(rows):
        for row in rows:
            course_table.append(
                {"cno": row[0], "name": row[1], "credit": row[2]})
    else:
        cursor.close()
        conn.close()
        return {"status": "failure", "data": []}
    cursor.close()
    conn.close()
    return {"status": "success", "data": course_table}


@app.route("/all/getCourseScheduleTable", methods=["GET"])
def getCourseScheduleTable():
    """
    获得所有的课程计划
    :return:
    """
    stu_course_list = []
    conn = psycopg2.connect(database="CourseSelectionSystem", user="gaussdb",
                            password="PommesPeter@123", host="10.0.0.3", port="15432")
    cursor = conn.cursor()
    cursor.execute(
        f"select cno, semester, day, index, classroom, optional, selected, startweek, endweek, schedule.coursecode, course.name from schedule join course on course.coursecode=schedule.coursecode")
    rows = cursor.fetchall()
    if len(rows):
        for row in rows:
            stu_course_list.append(
                {"cno": row[0], "semester": row[1], "day": row[2], "index": row[3], "classroom": row[4],
                 "optional": row[5], "selected": row[6], "startweek": row[7], "endweek": row[8], "coursecode": row[9],
                 "name": row[10]})
    else:
        cursor.close()
        conn.close()
        return {"status": "failure", "data": []}
    cursor.close()
    conn.close()
    return {"status": "success", "data": stu_course_list}
