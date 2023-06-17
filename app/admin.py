from django.contrib import admin
from .models import *;



class CustomSchool(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'school_dice_code', 'district', 'block', 'examination_center_code']
    list_display_links = ['id', 'school_name']
    search_fields = ['school_name', 'school_dice_code', 'district', 'block', 'examination_center_code']
    list_filter = ['district']


class CustomStudent(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'scholar_no', 'roll_no', 'father_name', 'mother_name', 'dob', 'school', 'student_class']
    list_display_links = ["id", "student_name"]
    search_fields = ['student_name', 'scholar_no', 'roll_no', 'father_name', 'mother_name', 'dob', 'school', 'student_class']
    list_filter = ['school', 'student_class']

class CustomStudentMark(admin.ModelAdmin):
    list_display = ['id', 'student', 'hindi', 'english', 'maths', 'sanskrit', 'environmental_studies', 'work_education', 'physical', 'arts', 'science', 'social_science', 'hindi_20', 'hindi_80', 'hindi_100', 'english_20', 'english_80', 'english_100', 'maths_20', 'maths_80', 'maths_100', 'science_20', 'science_80', 'science_100', 'sanskrit_20', 'sanskrit_80', 'sanskrit_100', 'social_science_20', 'social_science_80', 'social_science_100', 'work_education_20', 'work_education_80', 'work_education_100', 'arts_20', 'arts_80', 'arts_100', 'physical_20', 'physical_80', 'physical_100']
    list_display_links = ['id', 'student']
    search_fields = ['student']

class CustomMarksheet(admin.ModelAdmin):
    list_display = ['student', 'marksheet_id', 'total_grade', 'percentage', 'result', 'shreni', 'examination_date', 'report_card']
    list_display_links = ['student', 'marksheet_id']
    search_fields = ['student','marksheet_id', 'result', 'shreni']
    list_filter = ['result', 'shreni']

admin.site.register(SchoolDetail, CustomSchool)
admin.site.register(StudentDetail, CustomStudent)
admin.site.register(StudentMark, CustomStudentMark)
admin.site.register(Marksheet, CustomMarksheet)
