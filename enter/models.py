from django.db import models

# Create your models here.
class Post(models.Model):
    ism_familya = models.CharField(max_length=200)
    guruhi = models.CharField(max_length=200)
    umumiy_bali  = models.IntegerField()
    choices1 = (
        ("Passed", "O`tdi"),
        ("failed","O`ta olmadi")
    )
    testda_ishtirok_etishi= models.CharField(
        max_length= 6,
        choices = choices1,
        default = "O`tdi"
    )
    exams = (
        ("kunlik imtihon", "kunlik imtihon"),
        ("haftalik imtihon", "haftalik imtihon"),
        ("Oylik Imtihon", "Oylik Imtihon"),
        ("Yillik Imtihon", "Yillik Imtihon"),
    )
    exam_day= models.CharField(
        max_length= 22 ,
        choices = exams,
        default= 'Haftalik'
    )
    exam_date= models.DateField()

    class Meta:
        ordering = ['-umumiy_bali']
        db_table = "web_member"
    def __str__(self):
        return str(self.umumiy_bali) + '/' + self.ism_familya
class MyfutureForm(models.Model):
    ism_familyangiz = models.CharField(max_length=200)
    Telefon_raqamingiz = models.CharField(max_length=30)
    KURSGA_YOZILISh = [
        ('IELTS','IELTS'),
        ('PreIELTS','PreIELTS'),
        ('Matematika','Matematika'),
        ('Fizika','Fizika'),
        ('bolalar matematikasi','bolalar matematikasi'),
        ('Kimyo','Kimyo'),
        ('Biologiya','Biologiya'),

    ]
    Qaysi_kursga_yozilmoqchisiz = models.CharField(
        max_length=800, 
        choices=KURSGA_YOZILISh,
        default='IELTS')
    def __str__(self):
        return self.ism_familyangiz
    class Meta:
        db_table = 'MyfutureFormmember'
class Course_data(models.Model):
    name = models.CharField(max_length=150)
    cost_course = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    teacher = models.CharField(max_length=150)
    time = models.CharField(max_length=20, default='2 soat')
    students = models.IntegerField(default=30)
class Course_item(models.Model):
    name = models.CharField(max_length=150)
    cost = models.IntegerField(default=200000)
    good = models.CharField(max_length=150)
    good1 = models.CharField(max_length=150)
    good2 = models.CharField(max_length=150)
    good3 = models.CharField(max_length=150)
    good4 = models.CharField(max_length=150)
class Image_class(models.Model):
    img = models.ImageField(upload_to='images/')

class Mentorlar(models.Model):
    name = models.CharField(max_length=150)
    fani = models.CharField(max_length=150)
    izoh = models.CharField(max_length=200)
    rasmi = models.ImageField(upload_to='images/')
    telegram_linki = models.CharField(max_length=300)
    telephone = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Feedbacks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    message = models.CharField(max_length=350)