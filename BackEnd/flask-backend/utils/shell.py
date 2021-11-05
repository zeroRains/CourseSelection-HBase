import os

# os.system("pip install pandas -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com")
import happybase
from utils.config import config


def getNotSelectedCourse_stu(userid):
    """
    学生可以退课的接口
    :param userid:
    :return:
    """
    conn = happybase.Connection("127.0.0.1", 9090)
    record = conn.table(config["table"]["record"])
    course = conn.table(config["table"]["course"])
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
                str(val[bytes(config["name"]["课程课号"], "ascii")], "utf-8"))
        iters = course.scan()
        for key, val in iters:
            if str(key, 'utf-8') in courses:
                res.append({
                    "coursecode": str(val[bytes(config["name"]["课号"], "ascii")], "utf-8"),
                    "name": str(val[bytes(config["name"]["名称"], "ascii")], "utf-8"),
                    "credit": str(val[bytes(config["name"]["学分"], "ascii")], "utf-8"),
                })
        return {"status": "success", "data": res}


# m = md5()
userid = sno = 1900300101
cno = 2020199
passwd = 123456
print("?????")
getNotSelectedCourse_stu(userid)

conn = happybase.Connection("127.0.0.1", 9090)
record = conn.table(config["table"]["record"])
course = conn.table(config["table"]["course"])
selected_course = []
res_data = []
fill = f"SingleColumnValueFilter ('studentid', 'studentid', =, 'binary:111')"
iters = record.scan(filter=fill)
print(iters is None)
if iters is not None:
    for key, val in iters:
        selected_course.append(val[bytes(config["name"]["课程课号"], 'ascii')])
    selected_course = set(selected_course)
iters = course.scan()
# conn.close()
for key, val in iters:
    if str(key, "utf-8") not in selected_course:
        res_data.append({"coursecode": str(key, 'utf-8'),
                         "name": str(val[bytes(config["name"]["名称"], 'ascii')], "utf-8"),
                         "credit": str(val[bytes(config["name"]["学分"], 'ascii')], "utf-8"),
                         "time": str(val[bytes(config["name"]["学年"], 'ascii')], "utf-8"),
                         "teacher": str(val[bytes(config["name"]["老师"], 'ascii')], "utf-8"), })
print()

conn = happybase.Connection("127.0.0.1", 9090)
record = conn.table(config["table"]["record"])
courses = conn.table(config["table"]["course"])
res_data = []
tempdata = record.scan()
fill = f"SingleColumnValueFilter ('studentid', 'studentid', =, 'binary:{userid}')"
iters = record.scan(filter=fill)

for key, val in iters:
    course = courses.row(str(val[bytes(config["name"]["课程课号"], "ascii")], 'utf-8'))
    res_data.append({"name": str(course[bytes(config["name"]["名称"], 'ascii')], 'utf-8'),
                     "coursecode": str(course[bytes(config["name"]["课号"], 'ascii')], 'utf-8'),
                     "credit": str(course[bytes(config["name"]["学分"], 'ascii')], 'utf-8'),
                     })
conn.close()
print(userid)

conn = happybase.Connection("127.0.0.1", 9090)

table = conn.table("record")
for k, v in table.scan(filter="SingleColumnValueFilter ('score', 'score', !=, 'binary:77') "):
    print()
# tmp = table.scan()
# for data in tmp:
#     cmd = str(data[1][bytes("sinfo:password","ascii")])
#     cmd2 =  str(data[1][bytes("sinfo:password","ascii")],'utf-8')
#     print()
# table.put("1900300110",{"sinfo:sname":"钟离"})
print()
