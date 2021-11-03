import happybase

conn = happybase.Connection("127.0.0.1", 9090)

conn.create_table("student",{"sinfo":{},"studies":{}})
conn.create_table("course",{"cinfo":{},"teaching":{}})
conn.create_table("record",{"courseid":{},"studentid":{},"score":{}})

print( conn.tables())

