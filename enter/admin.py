from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BookAdmin(ImportExportModelAdmin):
    list_display = ('ism_familyangiz', 'Telefon_raqamingiz','Qaysi_kursga_yozilmoqchisiz')
    pass
class BookAdmin2(admin.ModelAdmin):
    list_display = ('name','cost_course','image','teacher')

admin.site.register(MyfutureForm, BookAdmin)
admin.site.register(Course_data , BookAdmin2)

class BookAdmin3(ImportExportModelAdmin):
    list_display = ('ism_familya','guruhi','umumiy_bali','testda_ishtirok_etishi','exam_day','exam_date')
    pass
admin.site.register(Post,BookAdmin3)

class Bookadmin(admin.ModelAdmin):
    list_display = ('name','cost','good','good1','good2','good3','good4')
admin.site.register(Course_item,Bookadmin)

class Bookadmin4(admin.ModelAdmin):
    list_display = ('name', 'fani', 'izohi', 'telegram_linki','telephone','rasmi')

admin.site.register(Image_class)
admin.site.register(Mentorlar)
class Bookadmin5(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'message')

admin.site.register(Feedbacks, Bookadmin5)