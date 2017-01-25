import MySQLdb


def printtable(cursor):
	results = cursor.fetchall()
	x = []
	y = []
	z = '|'
	se = '+' 


	for d in cursor.description:
		x.append(max(d[2], len(d[0])))
		y.append(d[0])

	for w in x:
	    z += " %-"+"%ss |" % (w,)
	    se += '-'*w + '--+'

	print(se)
	print(z % tuple(y))
	print(se)
	for row in results:
	    print(z % row)
	print(se)



cnx = MySQLdb.connect(host="10.5.18.101",user="14CS10003",passwd="btech14",db="14CS10003")
cursor = cnx.cursor()
cnx.commit()

print("i. List all the Courses taught by the teacher - \"PPC\".\n\n")
sql = "SELECT Courses.cno,Courses.Cname FROM teaches,teacher,Courses WHERE teacher.name=\"PPC\" AND teaches.tid=teacher.tid AND Courses.cno=teaches.cno;"
cursor.execute(sql)
printtable(cursor)


print("\nii. List all students registered in the courses taught by \"PPC\".\n\n")
sql = "SELECT DISTINCT student.sid,student.name FROM student,enrolled,teaches,teacher WHERE teacher.name=\"PPC\" AND teacher.tid=teaches.tid AND teaches.cno=enrolled.cno AND enrolled.sid=student.sid;"
cursor.execute(sql)
printtable(cursor)

print("\nii. List all students registered in the courses taught by \"PPC\".\n\n")
sql = "SELECT DISTINCT student.sid,student.name FROM student,enrolled,teaches,teacher WHERE teacher.name=\"PPC\" AND teacher.tid=teaches.tid AND teaches.cno=enrolled.cno AND enrolled.sid=student.sid;"
cursor.execute(sql)
printtable(cursor)

print("\niii. List the timings of all courses in Class-Room \"NC142\".\n\n")
sql = "SELECT Timings.day,Timings.starttime,Timings.endtime FROM Timings WHERE Timings.roomno=\"NC142\";"
cursor.execute(sql)
printtable(cursor)

print("\niv. List the name of the students who received the highest marks in the courses taught by \"PPC\"\n\n")
sql="SELECT student.name,enrolled.cno,enrolled.marks FROM (SELECT enrolled.cno,MAX(enrolled.marks) AS mark FROM enrolled,student,teacher,teaches WHERE teacher.name=\"PPC\" AND teacher.tid=teaches.tid AND enrolled.sid=student.sid AND enrolled.cno=teaches.cno GROUP BY enrolled.cno) AS x,enrolled,student WHERE enrolled.marks=x.mark AND enrolled.cno=x.cno AND enrolled.sid=student.sid;"
cursor.execute(sql)
printtable(cursor)

print("v. List the students who have received a grade of \"EX\" in the largest number of courses\"\n\n")
sql=" SELECT tb2.sid,tb2.name FROM (SELECT tb1.sid,tb1.name,COUNT(tb1.grade) as cnt FROM (SELECT ALL student.sid,student.name,enrolled.grade FROM student,enrolled WHERE enrolled.grade=\"EX\" AND enrolled.sid=student.sid) as tb1 GROUP BY tb1.sid) as tb2 WHERE tb2.cnt>=(SELECT MAX(tb2_.cnt2)  FROM (SELECT tb1_.sid,COUNT(tb1_.grade) as cnt2       FROM (SELECT ALL student.sid,enrolled.grade FROM student,enrolled WHERE enrolled.grade=\"EX\" AND enrolled.sid=student.sid) as tb1_ GROUP BY tb1_.sid) as tb2_);"
cursor.execute(sql)
printtable(cursor)

cnx.close()