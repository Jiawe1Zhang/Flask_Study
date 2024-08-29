from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "/Users/juswin/Desktop/flask_study/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "abc"

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True) #主键
    name = db.Column(db.String(64),nullable=False)
    gender = db.Column(db.Enum("男","女"),nullable=False)
    phone = db.Column(db.String(11))
    grades = db.relationship("Grade", backref = "student") # 定义关系属性grades；在Grade中添加student属性，指向关联的Student实例



class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True) #主键
    name = db.Column(db.String(64),nullable=False)


class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True) #主键
    name = db.Column(db.String(64),nullable=False)
    gender = db.Column(db.Enum("男","女"),nullable=False)
    phone = db.Column(db.String(11))


class Grade(db.Model):
    __tablename__ = "grade"
    id = db.Column(db.Integer, primary_key=True) #主键
    course_name = db.Column(db.String(64), nullable=False)
    grade = db.Column(db.String(3), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

with app.app_context():
    db.create_all()
    #db.drop_all()



if __name__ == '__main__':
    app.run()
    