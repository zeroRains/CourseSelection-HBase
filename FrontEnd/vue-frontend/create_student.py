import requests


# 学生生成计划

snos = [1900100110, 1900300201, 1900200401, 1900400302, 1900300102]
names = ["甘雨", "钟离", "重云", "凝光", "氪晴"]


for sno, name in zip(snos, names):
    t = requests.post(
        f"http://10.33.14.231:5000/stu/stuRegister/sno={sno}&name={name}&passwd=123456")
    print(t)
    print(t.text)


# 老师生成计划
tnos = [12345, 33333, 11111, 22222]
names = ["琴", "温迪", "迪卢克", "芭芭拉"]

for tno, name in zip(tnos, names):
    t = requests.post(
        f"http://10.33.14.231:5000/teacher/teacherRegister/tno={tno}&name={name}&passwd=123456")
    print(t)
    print(t.text)

# print(requests.post(
#     'http://10.33.14.231:5000/teacher/teacherRegister/tno=12234&name=wwww&passwd=123456').text)
