from django.contrib import admin
from .models import *;



class CustomSchool(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'school_dice_code', 'district', 'block', 'examination_center_code']
    list_display_links = ['id', 'school_name']

class CustomStudent(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'scholar_no', 'roll_no', 'father_name', 'mother_name', 'dob', 'school']
    list_display_links = ["id", "student_name"]

class CustomStudentMark(admin.ModelAdmin):
    list_display = ['id', 'student']
    list_display_links = ['id', 'student']

class CustomMarksheet(admin.ModelAdmin):
    list_display = ['student', 'marksheet_id', 'total_grade', 'percentage', 'result', 'shreni', 'examination_date', 'report_card']
    list_display_links = ['student', 'marksheet_id']


admin.site.register(SchoolDetail, CustomSchool)
admin.site.register(StudentDetail, CustomStudent)
admin.site.register(StudentMark, CustomStudentMark)
admin.site.register(Marksheet, CustomMarksheet)
