from django.db import models
from django.core.validators import MinValueValidator



class SchoolDetail(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    school_name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    block = models.CharField(max_length=255)

    # Code Fields
    kendra_code = models.CharField(max_length=15)
    school_dice_code = models.CharField(max_length=255)      # dice code

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

    def __str__(self):
        return self.student_name



# NOTE: AT Time of Production Remove Default values of Examination Date and Dateofbirth
class MarksheetFormat_1(models.Model):
    # Marksheet Details
    id = models.AutoField(primary_key=True, editable=False)
    marksheet_id = models.CharField(max_length=20, default="")
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    total_grade = models.CharField(max_length=3)
    examination_date = models.DateField()
    report_card = models.FileField(upload_to='pdf_files/', max_length=255, default=None, null=True)

    # Marks
    hindi = models.CharField(max_length=5)
    english = models.CharField(max_length=5)
    maths = models.CharField(max_length=5)
    environmental_studies = models.CharField(max_length=5)
    sanskrit = models.CharField(max_length=5)
    arts = models.CharField(max_length=5)
    working_education = models.CharField(max_length=5)
    physical = models.CharField(max_length=5)


# NOTE: MarksheetFormat_1 and MarksheetFormat_2 has only 1 difference i.e. Subject 9
class MarksheetFormat_2(models.Model):
    # marksheet details
    id = models.AutoField(primary_key=True, editable=False)
    marksheet_id = models.CharField(max_length=20, default="")
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    total_grade = models.CharField(max_length=3)
    examination_date = models.DateField()
    report_card = models.FileField(upload_to='pdf_files/', max_length=255, default=None, null=True)

    # marks
    hindi = models.CharField(max_length=5)
    english = models.CharField(max_length=5)
    science = models.CharField(max_length=5)
    social_science = models.CharField(max_length=5)
    maths = models.CharField(max_length=5)
    sanskrit = models.CharField(max_length=5)
    work_education = models.CharField(max_length=5)
    physical = models.CharField(max_length=5)
    arts = models.CharField(max_length=5)  # this subject is only for 8th class students


class MarksheetFormat_3(models.Model):
    # marksheet details
    id = models.AutoField(primary_key=True, editable=False)
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    marksheet_id = models.CharField(max_length=20, default="")
    result = models.CharField(max_length=10)
    shreni = models.CharField(max_length=10)
    percentage = models.CharField(max_length=10)
    examination_date = models.DateField()
    report_card = models.FileField(upload_to='pdf_files/', max_length=255, default=None, null=True)

    # marks
    hindi_20 = models.CharField(max_length=3)
    hindi_80 = models.CharField(max_length=3)
    hindi_100 = models.CharField(max_length=3)
    english_20 = models.CharField(max_length=3)
    english_80 = models.CharField(max_length=3)
    english_100 = models.CharField(max_length=3)
    maths_20 = models.CharField(max_length=3)
    maths_80 = models.CharField(max_length=3)
    maths_100 = models.CharField(max_length=3)
    science_20 = models.CharField(max_length=3)
    science_80 = models.CharField(max_length=3)
    science_100 = models.CharField(max_length=3)
    sanskrit_20 = models.CharField(max_length=3)
    sanskrit_80 = models.CharField(max_length=3)
    sanskrit_100 = models.CharField(max_length=3)
    social_science_20 = models.CharField(max_length=3)
    social_science_80 = models.CharField(max_length=3)
    social_science_100 = models.CharField(max_length=3)
    work_education_20 = models.CharField(max_length=3)
    work_education_80 = models.CharField(max_length=3)
    work_education_100 = models.CharField(max_length=3)
    arts_20 = models.CharField(max_length=3)
    arts_80 = models.CharField(max_length=3)
    arts_100 = models.CharField(max_length=3)
    physical_20 = models.CharField(max_length=3)
    physical_80 = models.CharField(max_length=3)
    physical_100 = models.CharField(max_length=3)
