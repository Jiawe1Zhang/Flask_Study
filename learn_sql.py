from sql_study import Student, db, app, Grade

""" #增
s1 = Student(name = "张三", gender = "男", phone = "18745678900" )
s2 = Student(name = "李四", gender = "男", phone = "15745678901" )
s3 = Student(name = "张家玮", gender = "男", phone = "18857850005" )
s4 = Student(name = "季心雨", gender = "女", phone = "12394378900" )
s5 = Student(name = "路人甲", gender = "女", phone = "14545672342" )

grade1 = Grade(course_name = "数学" ,grade = 135 ,student_id = 1)
grade2 = Grade(course_name = "语文" ,grade = 66 ,student_id = 2)
grade3 = Grade(course_name = "英语" ,grade = 120 ,student_id = 3)
grade4 = Grade(course_name = "语文" ,grade = 89 ,student_id = 1)
grade5 = Grade(course_name = "物理" ,grade = 88 ,student_id = 2)

with app.app_context():
    db.session.add_all([s1,s2,s3,s4,s5])
    db.session.add_all([grade1,grade2,grade3,grade4,grade5])
    db.session.commit()
 """

# 查
""" with app.app_context():
    stu = Student.query.get(1)
    print(stu)
    print(stu.name)
    print(stu.gender)
    print(stu.phone)

with app.app_context():
    stu = Student.query.all()
    for i in stu:
        print(i.name)

with app.app_context():
    # 条件查询
    stu = Student.query.filter(Student.id >=2)
    for i in stu:
        print(i.name, i.id) """


""" with app.app_context():
    stu = Student.query.filter_by(name="张三").filter(Student.id >=2)
    for i in stu:
        print(i.name)
 """

with app.app_context():
    # 1 对 多
    stu = Student.query.get(1)
    print(stu.grades)
    print(stu)
    for i in stu.grades:
        print(stu.name,stu.gender, i.course_name, i.student_id, i.grade)
    
    # 多对1
    mid = Grade.query.filter(Grade.grade == 120)
    for i in mid:
        print(i.student_id,i.student.name,i)

# 改
# 第一种方式
""" with app.app_context():
    stu = Student.query.filter(Student.id == 1).update({"name":"李四"})
    db.session.commit()

with app.app_context():
    stu = Student.query.filter(Student.gender == "男").update({"gender":"女"})
    print(stu) #改了多少条数据
    db.session.commit() """

# 第二种方式
""" with app.app_context():
    stu = Student.query.filter(Student.gender == "女").first()
    stu.gender = "男"
    db.session.add(stu)
    db.session.commit() """



#删

""" with app.app_context():
    stu = Student.query.filter(Student.id >= 2).delete()
    print(stu)
    db.session.commit() """
 
