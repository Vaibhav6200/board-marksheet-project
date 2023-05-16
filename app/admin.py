from django.contrib import admin
from .models import *;



class CustomSchool(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'school_dice_code', 'district', 'block', 'kendra_code']
    list_display_links = ['id', 'school_name']

class CustomStudent(admin.ModelAdmin):
    list_display = ['id', 'school', 'scholar_no', 'roll_no', 'student_name', 'father_name', 'mother_name', 'dob']
    list_display_links = ["id", "student_name"]


class CustomMarksheet1(admin.ModelAdmin):
    list_display = ["marksheet_id", "student", "total_grade", "examination_date", "hindi", "english", "maths", "environmental_studies", "sanskrit", "arts", "working_education", "physical", "report_card"]
    list_display_links = ['student', 'marksheet_id']


class CustomMarksheet2(admin.ModelAdmin):
    list_display = ['marksheet_id', 'student', 'total_grade', 'examination_date', 'hindi', 'english', 'science', 'social_science', 'maths', 'sanskrit', 'work_education', 'physical', 'arts', 'report_card']
    list_display_links = ['student', 'marksheet_id']


class CustomMarksheet3(admin.ModelAdmin):
    list_display = ['marksheet_id', 'student', 'result', 'shreni', 'percentage', 'examination_date', 'hindi_100', 'english_100', 'science_100', 'social_science_100', 'maths_100', 'sanskrit_100', 'work_education_100', 'physical_100', 'arts_100', 'report_card']
    list_display_links = ['student', 'marksheet_id']


["student", "marksheet_id", "result", "shreni", "percentage", "examination_year", "report_card"]
admin.site.register(SchoolDetail, CustomSchool)
admin.site.register(StudentDetail, CustomStudent)
admin.site.register(MarksheetFormat_1, CustomMarksheet1)
admin.site.register(MarksheetFormat_2, CustomMarksheet2)
admin.site.register(MarksheetFormat_3, CustomMarksheet3)
