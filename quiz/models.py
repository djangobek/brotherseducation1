from django.db import models

from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50,  verbose_name="Kurs nomi")
   question_number = models.PositiveIntegerField( verbose_name="Savollar soni")
   total_marks = models.PositiveIntegerField( verbose_name="Umumiy BAli")
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name="Qaysi_test")
    marks=models.PositiveIntegerField(verbose_name="baholari")
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE , verbose_name="Ismi")
    exam = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name="Qaysi imtihon")
    marks = models.PositiveIntegerField(verbose_name="Bahosi")
    date = models.DateTimeField(auto_now=True)

