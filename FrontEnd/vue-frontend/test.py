import requests
path = "http://10.33.14.231:5000/"
userid = "3b598a74-a3e4-3a14-9262-eb05fc90fbfd"
t = requests.get(path+'all/getCourseTable')
print(t.text)
print(t)
