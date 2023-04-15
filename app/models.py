from django.db import models
from django.core.validators import MinValueValidator



# NOTE: AT Time of Production Remove Default values of Examination Date and Dateofbirth
class Marksheet(models.Model):
    markSheetCode = models.AutoField(primary_key=True, editable=False)

    # Student Details
    scholar_no = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField(default="2002-02-22")
    student_class = models.PositiveSmallIntegerField()

    # School Details
    school_name = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    school_dice_code = models.CharField(max_length=255)      # dice code
    examination_center = models.CharField(max_length=255)
    examination_center_code = models.CharField(max_length=50)

    # Marksheet Details
    marksheet_id = models.CharField(max_length=20, default="")
    grade = models.CharField(max_length=3)
    average = models.PositiveSmallIntegerField()
    examination_date = models.DateField(default="2002-08-12")
    subject_1 = models.PositiveSmallIntegerField()
    subject_2 = models.PositiveSmallIntegerField()
    subject_3 = models.PositiveSmallIntegerField()
    subject_4 = models.PositiveSmallIntegerField()
    subject_5 = models.PositiveSmallIntegerField()
    subject_6 = models.PositiveSmallIntegerField()
    subject_7 = models.PositiveSmallIntegerField()
    subject_8 = models.PositiveSmallIntegerField()
    subject_9 = models.PositiveSmallIntegerField()       # this subject is only for 8th class students

    report_card = models.FileField(upload_to='pdf_files/', max_length=255, default=None, null=True)

