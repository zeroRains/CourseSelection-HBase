import requests
path = "http://10.33.14.231:5000/"
userid = "1d892a74-d740-3198-9c1f-db4f132ff577"
cno = "2022426"
coursecode = "BT0300099X0"
semester = "2020-2021下"
classroom = "14103*"
time = "1,1,1,8"
option = '62'
sql = path+f'stu/isChoosible/coursecode='+coursecode
sql = path+"stu/selectCourse/userid=3b598a74-a3e4-3a14-9262-eb05fc90fbfd&cno=2022418"
print(sql)
t = requests.post(sql)
print(t.text)
print(t)
