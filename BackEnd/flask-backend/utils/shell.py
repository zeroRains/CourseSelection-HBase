import os

# os.system("pip install pandas -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com")
import happybase

conn = happybase.Connection("127.0.0.1", 9090)
table = conn.table("student")
table.put("1900300110",{"sinfo:sname":"钟离"})
