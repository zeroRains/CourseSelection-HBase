import requests
path = "http://10.33.14.231:5000/"
userid = "1d892a74-d740-3198-9c1f-db4f132ff577"
cno = "2022426"
coursecode = "BT0400350X0"
semester = "2020-2021下"
classroom = "14103*"
time = "1,1,1,8"
option = '62'
t = requests.get(path+f'teacher/getTeachTable/userid='+userid)
print(t.text)
print(t)
