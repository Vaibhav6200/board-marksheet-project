from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
from .models import *
from .pdf1Annotator import annotatePDF
from .pdf2Annotator import annotatePDF_format2
from .pdf3Annotator import annotatePDF_format3

from django.core.files import File
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.db.models import Q



def process_marksheet_1(data):
    rows = data.shape[0]

    for row in range(rows):
        # Fetch Individual Student Data
        scholar_no = data.loc[row, 'scholar_no']
        roll_no = data.loc[row, 'roll_no']
        student_name = data.loc[row, 'student_name']
        father_name = data.loc[row, 'father_name']
        mother_name = data.loc[row, 'mother_name']
        dob = data.loc[row, 'dob']
        student_class = data.loc[row, 'student_class']
        school_name = data.loc[row, 'school_name']
        district = data.loc[row, 'district']
        block = data.loc[row, 'block']
        school_dice_code = data.loc[row, 'school_dice_code']
        examination_center_code = data.loc[row, 'examination_center_code']
        marksheet_id = data.loc[row, 'marksheet_id']
        total_grade = data.loc[row, 'total_grade']
        examination_date = data.loc[row, 'examination_date']
        hindi = data.loc[row, 'hindi']
        english = data.loc[row, 'english']
        maths = data.loc[row, 'maths']
        sanskrit = data.loc[row, 'sanskrit']
        environmental_studies = data.loc[row, 'environmental_studies']
        work_education = data.loc[row, 'work_education']
        physical = data.loc[row, 'physical']
        arts = data.loc[row, 'arts']

        report_data = {
            'scholar_no': str(scholar_no),
            'roll_no': str(roll_no),
            'student_name': student_name,
            'father_name': father_name,
            'mother_name': mother_name,
            'dob': dob,
            'student_class': student_class,
            'school_name': school_name,
            'block': block,
            'district': district,
            'school_dice_code': str(school_dice_code),
            'examination_center_code': str(examination_center_code),
            'marksheet_id': str(marksheet_id),
            'overall_grade': total_grade,
            'examination_date': examination_date,
            'hindi': hindi,
            'english': english,
            'maths': maths,
            'sanskrit': sanskrit,
            'environmental_studies': environmental_studies,
            'arts': arts,
            'work_education': work_education,
            'physical': physical
        }


        dob_datetime = datetime.strptime(dob, '%d-%b-%y')       # Convert date string to datetime object
        dob_formatted = dob_datetime.strftime('%Y-%m-%d')       # Convert datetime object to the desired format

        exam_date_datetime = datetime.strptime(examination_date, '%d-%b-%y')
        exam_date_formatted = exam_date_datetime.strftime('%Y-%m-%d')


        # Generate our Marksheet
        output_file_name = annotatePDF(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # *** Add Details in Database ***
        # Step 1: Create School Table
        # NOTE: Check if school with the same details already exists
        school_obj = None
        try:
            school_obj = SchoolDetail.objects.get(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
        except SchoolDetail.DoesNotExist:
            # Create School object if it doesn't exist
            school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
            school_obj.save()


        # Step 2: Create Student Table (Foreign Key on School)
        student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob_formatted, student_class=student_class)
        student_obj.save()

        # Step 3: Create Marksheet Table (Foreign Key on Student)
        marksheet_obj = MarksheetFormat_1(marksheet_id=marksheet_id, student=student_obj, total_grade=total_grade, examination_date=exam_date_formatted, hindi=hindi, english=english, maths=maths, sanskrit=sanskrit, environmental_studies=environmental_studies, arts=arts, work_education=work_education, physical=physical)
        marksheet_obj.report_card.name = pdf_file_path
        marksheet_obj.save()


def process_marksheet_2(data):
    rows = data.shape[0]
    for row in range(rows):
        # Fetch Individual Student Data
        scholar_no = data.loc[row, 'scholar_no']
        roll_no = data.loc[row, 'roll_no']
        student_name = data.loc[row, 'student_name']
        father_name = data.loc[row, 'father_name']
        mother_name = data.loc[row, 'mother_name']
        dob = data.loc[row, 'dob']
        student_class = data.loc[row, 'student_class']
        school_name = data.loc[row, 'school_name']
        district = data.loc[row, 'district']
        block = data.loc[row, 'block']
        school_dice_code = data.loc[row, 'school_dice_code']
        examination_center_code = data.loc[row, 'examination_center_code']
        marksheet_id = data.loc[row, 'marksheet_id']
        total_grade = data.loc[row, 'total_grade']
        examination_date = data.loc[row, 'examination_date']
        hindi = data.loc[row, 'hindi']
        english = data.loc[row, 'english']
        maths = data.loc[row, 'maths']
        sanskrit = data.loc[row, 'sanskrit']
        science = data.loc[row, 'science']
        social_science = data.loc[row, 'social_science']
        work_education = data.loc[row, 'work_education']
        physical = data.loc[row, 'physical']
        arts = data.loc[row, 'arts']

        report_data = {
            'scholar_no': str(scholar_no),
            'roll_no': str(roll_no),
            'student_name': student_name,
            'father_name': father_name,
            'mother_name': mother_name,
            'dob': dob,
            'student_class': student_class,
            'school_name': school_name,
            'block': block,
            'district': district,
            'school_dice_code': str(school_dice_code),
            'examination_center_code': str(examination_center_code),
            'marksheet_id': str(marksheet_id),
            'examination_date': examination_date,
            'total_grade': total_grade,
            'hindi': hindi,
            'english': english,
            'maths': maths,
            'sanskrit': sanskrit,
            'science': science,
            'social_science': social_science,
            'arts': arts,
            'work_education': work_education,
            'physical': physical
        }


        dob_datetime = datetime.strptime(dob, '%d-%b-%y')       # Convert date string to datetime object
        dob_formatted = dob_datetime.strftime('%Y-%m-%d')       # Convert datetime object to the desired format

        exam_date_datetime = datetime.strptime(examination_date, '%d-%b-%y')
        exam_date_formatted = exam_date_datetime.strftime('%Y-%m-%d')


        # Generate our Marksheet
        output_file_name = annotatePDF_format2(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # *** Add Details in Database ***
        # Step 1: Create School Table
        # NOTE: Check if school with the same details already exists
        school_obj = None
        try:
            school_obj = SchoolDetail.objects.get(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
        except SchoolDetail.DoesNotExist:
            # Create School object if it doesn't exist
            school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
            school_obj.save()


        # Step 2: Create Student Table (Foreign Key on School)
        student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob_formatted, student_class=student_class)
        student_obj.save()

        # Step 3: Create Marksheet Table (Foreign Key on Student)
        marksheet_obj = MarksheetFormat_2(marksheet_id=marksheet_id, student=student_obj, total_grade=total_grade, examination_date=exam_date_formatted, hindi=hindi, english=english, maths=maths, sanskrit=sanskrit, science=science, social_science=social_science, arts=arts, work_education=work_education, physical=physical)
        marksheet_obj.report_card.name = pdf_file_path
        marksheet_obj.save()


def process_marksheet_3(data):
    rows = data.shape[0]
    for row in range(rows):
        # Fetch Individual Student Data
        scholar_no = data.loc[row, 'scholar_no']
        roll_no = data.loc[row, 'roll_no']
        student_name = data.loc[row, 'student_name']
        father_name = data.loc[row, 'father_name']
        mother_name = data.loc[row, 'mother_name']
        dob = data.loc[row, 'dob']
        swayam_pathi = data.loc[row, 'swayam_pathi']
        student_class = data.loc[row, 'student_class']
        school_name = data.loc[row, 'school_name']
        district = data.loc[row, 'district']
        block = data.loc[row, 'block']
        school_dice_code = data.loc[row, 'school_dice_code']
        examination_center_code = data.loc[row, 'examination_center_code']
        marksheet_id = data.loc[row, 'marksheet_id']
        examination_date = data.loc[row, 'examination_date']
        result = data.loc[row, 'result']
        shreni = data.loc[row, 'shreni']
        percentage = data.loc[row, 'percentage']
        hindi_20 = data.loc[row, 'hindi_20']
        hindi_80 = data.loc[row, 'hindi_80']
        hindi_100 = data.loc[row, 'hindi_100']
        english_20 = data.loc[row, 'english_20']
        english_80 = data.loc[row, 'english_80']
        english_100 = data.loc[row, 'english_100']
        maths_20 = data.loc[row, 'maths_20']
        maths_80 = data.loc[row, 'maths_80']
        maths_100 = data.loc[row, 'maths_100']
        science_20 = data.loc[row, 'science_20']
        science_80 = data.loc[row, 'science_80']
        science_100 = data.loc[row, 'science_100']
        sanskrit_20 = data.loc[row, 'sanskrit_20']
        sanskrit_80 = data.loc[row, 'sanskrit_80']
        sanskrit_100 = data.loc[row, 'sanskrit_100']
        social_science_20 = data.loc[row, 'social_science_20']
        social_science_80 = data.loc[row, 'social_science_80']
        social_science_100 = data.loc[row, 'social_science_100']
        work_education_20 = data.loc[row, 'work_education_20']
        work_education_80 = data.loc[row, 'work_education_80']
        work_education_100 = data.loc[row, 'work_education_100']
        arts_20 = data.loc[row, 'arts_20']
        arts_80 = data.loc[row, 'arts_80']
        arts_100 = data.loc[row, 'arts_100']
        physical_20 = data.loc[row, 'physical_20']
        physical_80 = data.loc[row, 'physical_80']
        physical_100 = data.loc[row, 'physical_100']


        report_data = {
            'scholar_no': str(scholar_no),
            'roll_no': str(roll_no),
            'student_name': student_name,
            'father_name': father_name,
            'mother_name': mother_name,
            'dob': dob,
            'swayam_pathi': swayam_pathi,
            'school_name': school_name,
            'district': district,
            'marksheet_id': str(marksheet_id),
            "result": result,
            "shreni": shreni,
            "percentage": percentage,
            "hindi_20": hindi_20,
            "hindi_80": hindi_80,
            "hindi_100": hindi_100,
            "english_20": english_20,
            "english_80": english_80,
            "english_100": english_100,
            "maths_20": maths_20,
            "maths_80": maths_80,
            "maths_100": maths_100,
            "science_20": science_20,
            "science_80": science_80,
            "science_100": science_100,
            "sanskrit_20": sanskrit_20,
            "sanskrit_80": sanskrit_80,
            "sanskrit_100": sanskrit_100,
            "social_science_20": social_science_20,
            "social_science_80": social_science_80,
            "social_science_100": social_science_100,
            "work_education_20": work_education_20,
            "work_education_80": work_education_80,
            "work_education_100": work_education_100,
            "arts_20": arts_20,
            "arts_80": arts_80,
            "arts_100": arts_100,
            "physical_20": physical_20,
            "physical_80": physical_80,
            "physical_100": physical_100,
        }


        dob_datetime = datetime.strptime(dob, '%d-%b-%y')       # Convert date string to datetime object
        dob_formatted = dob_datetime.strftime('%Y-%m-%d')       # Convert datetime object to the desired format

        exam_date_datetime = datetime.strptime(examination_date, '%d-%b-%y')
        exam_date_formatted = exam_date_datetime.strftime('%Y-%m-%d')


        # Generate our Marksheet
        output_file_name = annotatePDF_format3(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # *** Add Details in Database ***
        # Step 1: Create School Table
        school_obj = None
        try:
            school_obj = SchoolDetail.objects.get(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
        except SchoolDetail.DoesNotExist:
            school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
            school_obj.save()

        # Step 2: Create Student Table (Foreign Key on School)
        student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob_formatted, student_class=student_class)
        student_obj.save()

        # Step 3: Create Marksheet Table (Foreign Key on Student)
        marksheet_obj = MarksheetFormat_3(marksheet_id=marksheet_id, student=student_obj, result=result, shreni=shreni, percentage=percentage, examination_date=exam_date_formatted, hindi_20 = hindi_20, hindi_80 = hindi_80, hindi_100 = hindi_100, english_20 = english_20, english_80 = english_80, english_100 = english_100, maths_20 = maths_20, maths_80 = maths_80, maths_100 = maths_100, science_20 = science_20, science_80 = science_80, science_100 = science_100, sanskrit_20 = sanskrit_20, sanskrit_80 = sanskrit_80, sanskrit_100 = sanskrit_100, social_science_20 = social_science_20, social_science_80 = social_science_80, social_science_100 = social_science_100, work_education_20 = work_education_20, work_education_80 = work_education_80, work_education_100 = work_education_100, arts_20 = arts_20, arts_80 = arts_80, arts_100 = arts_100, physical_20 = physical_20, physical_80 = physical_80, physical_100 = physical_100)
        marksheet_obj.report_card.name = pdf_file_path
        marksheet_obj.save()


def index(request):
    if request.method == "POST" and request.FILES['csv_file']:
        selected_format = request.POST.get("dropdown_button")
        csv_file = request.FILES['csv_file']
        data = pd.read_csv(csv_file)

        # Marksheet format 1
        if selected_format == "format_1":
            process_marksheet_1(data)

        # Marksheet Format 2
        elif selected_format == "format_2":
            process_marksheet_2(data)

        # Marksheet Format 3
        elif selected_format == "format_3":
            process_marksheet_3(data)

        return redirect('/')        # this helps in prevention of form resubmission on reloading page


    # MAKE SURE TO UPDATE THIS CONDITION
    details1 = MarksheetFormat_1.objects.all()
    details2 = MarksheetFormat_2.objects.all()
    details3 = MarksheetFormat_3.objects.all()

    params = {
        'details_1': details1,
        'details_2': details2,
        'details_3': details3,
        'combined_details': [details1, details2, details3],
    }

    return render(request, "index.html", params)



def search(request):
    query = request.GET.get('search')
    params = {}
    if query:
        results = MarksheetFormat_1.objects.filter(
            Q(roll_no=query) |
            Q(school_dice_code=query) |
            Q(scholar_no=query) |
            Q(student_name__icontains=query) |
            Q(school_name__icontains=query) |
            Q(school_name__icontains=query)
        )
        params['details'] = results
    else:
        results = MarksheetFormat_1.objects.all()
        params['details'] = results
    return render(request, "index.html", params)

