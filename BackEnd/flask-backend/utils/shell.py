import os

# os.system("pip install pandas -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com")
import happybase
from utils.config import config


# m = md5()
userid = sno = 1900300101
cno = 2020199
passwd = 123456

conn = happybase.Connection("127.0.0.1", 9090)
record = conn.table(config["table"]["record"])
courses = conn.table(config["table"]["course"])
res_data = []
fill = f"SingleColumnValueFilter ('studentid', 'studentid', =, 'binary:{userid}')"
iters = record.scan(filter=fill)

for key, val in iters:
    course = courses.row(str(val[bytes(config["name"]["课程课号"],"ascii")], 'utf-8'))
    res_data.append({"name": str(course[bytes(config["name"]["名称"], 'ascii')], 'utf-8'),
                     "coursecode": str(course[bytes(config["name"]["课号"], 'ascii')], 'utf-8'),
                     "credit": str(course[bytes(config["name"]["学分"], 'ascii')], 'utf-8'),
                     })
conn.close()
print(userid)


conn = happybase.Connection("127.0.0.1", 9090)

table = conn.table("record")
for k,v in table.scan(filter="SingleColumnValueFilter ('score', 'score', !=, 'binary:77') "):
    print()
# tmp = table.scan()
# for data in tmp:
#     cmd = str(data[1][bytes("sinfo:password","ascii")])
#     cmd2 =  str(data[1][bytes("sinfo:password","ascii")],'utf-8')
#     print()
# table.put("1900300110",{"sinfo:sname":"钟离"})
print()
