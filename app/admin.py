from django.contrib import admin
from .models import *;


class customMarksheet(admin.ModelAdmin):
    list_display = ['roll_no', 'student_name', 'marksheet_id', 'scholar_no', 'school_name', 'grade', 'average', 'examination_date', 'report_card']
    list_display_links = ['roll_no', 'student_name']
    search_fields = ['roll_no', 'student_name', 'school_name', 'block', 'district', 'school_dice_code', 'examination_center', 'scholar_no', 'dob', 'father_name', 'mother_name', 'markSheetCode', 'year_of_examination']
    list_filter = ['grade', 'examination_date','block', 'district', 'examination_center']


admin.site.register(Marksheet, customMarksheet)
