from django.db import models
from django.core.validators import MinValueValidator



class SchoolDetail(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    school_name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    block = models.CharField(max_length=255)

    # Code Fields
    examination_center_code = models.CharField(max_length=15)
    school_dice_code = models.CharField(max_length=255)      # dice code

    object = models.Manager

    def __str__(self):
        return self.school_name


class StudentDetail(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    school = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
    scholar_no = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField()

    # extra field
    student_class = models.CharField(max_length=10)
    swayam_pathi = models.CharField(max_length=10, default="")

    object = models.Manager

    def __str__(self):
        return self.student_name


class StudentMark(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    hindi = models.CharField(max_length=5, default="")
    english = models.CharField(max_length=5, default="")
    maths = models.CharField(max_length=5, default="")
    sanskrit = models.CharField(max_length=5, default="")
    environmental_studies = models.CharField(max_length=5, default="")
    work_education = models.CharField(max_length=5, default="")
    physical = models.CharField(max_length=5, default="")
    arts = models.CharField(max_length=5, default="")
    science = models.CharField(max_length=5, default="")
    social_science = models.CharField(max_length=5, default="")
    hindi_20 = models.CharField(max_length=3, default="")
    hindi_80 = models.CharField(max_length=3, default="")
    hindi_100 = models.CharField(max_length=3, default="")
    english_20 = models.CharField(max_length=3, default="")
    english_80 = models.CharField(max_length=3, default="")
    english_100 = models.CharField(max_length=3, default="")
    maths_20 = models.CharField(max_length=3, default="")
    maths_80 = models.CharField(max_length=3, default="")
    maths_100 = models.CharField(max_length=3, default="")
    science_20 = models.CharField(max_length=3, default="")
    science_80 = models.CharField(max_length=3, default="")
    science_100 = models.CharField(max_length=3, default="")
    sanskrit_20 = models.CharField(max_length=3, default="")
    sanskrit_80 = models.CharField(max_length=3, default="")
    sanskrit_100 = models.CharField(max_length=3, default="")
    social_science_20 = models.CharField(max_length=3, default="")
    social_science_80 = models.CharField(max_length=3, default="")
    social_science_100 = models.CharField(max_length=3, default="")
    work_education_20 = models.CharField(max_length=3, default="")
    work_education_80 = models.CharField(max_length=3, default="")
    work_education_100 = models.CharField(max_length=3, default="")
    arts_20 = models.CharField(max_length=3, default="")
    arts_80 = models.CharField(max_length=3, default="")
    arts_100 = models.CharField(max_length=3, default="")
    physical_20 = models.CharField(max_length=3, default="")
    physical_80 = models.CharField(max_length=3, default="")
    physical_100 = models.CharField(max_length=3, default="")
    object = models.Manager


class Marksheet(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    marks = models.ForeignKey(StudentMark, on_delete=models.CASCADE)
    marksheet_id = models.CharField(max_length=20, default="")
    total_grade = models.CharField(max_length=3, default="")
    examination_date = models.DateField()
    result = models.CharField(max_length=10, default="")
    shreni = models.CharField(max_length=10, default="")
    percentage = models.CharField(max_length=10, default="")
    report_card = models.FileField(upload_to='pdf_files/', max_length=255, default=None, null=True)

    object = models.Manager

