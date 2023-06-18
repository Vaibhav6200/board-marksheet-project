from datetime import datetime
from django.shortcuts import redirect, render
import pandas as pd
from .models import *
from .pdf1Annotator import annotatePDF
from .pdf2Annotator import annotatePDF_format2
from .pdf3Annotator import annotatePDF_format3
import os
from django.db.models import Q
from django.core.paginator import Paginator
from dateutil import parser
import zipfile
from django.conf import settings
from django.http import HttpResponse, FileResponse
import shutil


import os, io, zipfile
import requests
from django.http import HttpResponse



def filter_school(request, class_id):
    params = {}
    if request.method == "POST":
        district = request.POST.get("district", "")
        block = request.POST.get("block","")
        available_schools = SchoolDetail.objects.filter(Q(district__icontains=district) & Q(block__icontains=block))
        params['available_schools'] = available_schools

    schools = SchoolDetail.objects.all()
    districts = set()
    blocks = set()
    for school in schools:
        districts.add(school.district.lower().strip())
        blocks.add(school.block.lower().strip())

    params['class_id'] = class_id
    params['districts'] = districts
    params['blocks'] = blocks
    return render(request, "mainApp/filter_school.html", params)


def downloadAll(request):
    cwd = os.getcwd()
    zip_path = os.path.join(cwd, 'media', 'temp_ZIP.zip')
    zip_file = open(zip_path, 'rb')
    response = HttpResponse(zip_file, content_type='application/zip')
    response['Content-Disposition'] = 'attachment;'
    return response


def filter_student(request, class_id):
    params = {}
    if request.method == "POST":
        dice_code = request.POST.get('school_dice_code')
        marksheets = Marksheet.objects.filter(student__school__school_dice_code=dice_code)
        params['marksheets'] = marksheets

        cwd = os.getcwd()
        zip_path = os.path.join(cwd, 'media', 'temp_ZIP.zip')
        with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as myZip:

            for sheet in marksheets:
                name = sheet.report_card.name
                filepath = os.path.join(cwd, 'media', name)
                filename = name.split('\\')[-1]

                myZip.write(filepath, filename)

    params['class_id'] = class_id
    return render(request, "mainApp/filter_student.html", params)


def process_marksheet_1(data):
    rows = data.shape[0]

    for row in range(rows):
        # Fetch Individual Student Data
        scholar_no = int(data.loc[row, 'scholar_no'])
        roll_no = int(data.loc[row, 'roll_no'])
        student_name = data.loc[row, 'student_name']
        father_name = data.loc[row, 'father_name']
        mother_name = data.loc[row, 'mother_name']
        dob = data.loc[row, 'dob']
        student_class = data.loc[row, 'student_class']
        school_name = data.loc[row, 'school_name']
        district = data.loc[row, 'district']
        block = data.loc[row, 'block']
        school_dice_code = int(data.loc[row, 'school_dice_code'])
        examination_center_code = int(data.loc[row, 'examination_center_code'])
        marksheet_id = int(data.loc[row, 'marksheet_id'])
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

        dob_obj = datetime.strptime(dob, '%d-%m-%Y')
        dob_formatted = dob_obj.strftime('%Y-%m-%d')

        exam_date_datetime = datetime.strptime(dob, '%d-%m-%Y')
        exam_date_formatted = exam_date_datetime.strftime('%Y-%m-%d')

        # Generate our Marksheet
        output_file_name = annotatePDF(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # *** Add Details in Database ***
        # Step 1: Create School Table
        # NOTE: Check if school with the same details already exists
        school_obj = None
        try:
            school_obj = SchoolDetail.objects.get(school_name=school_name, district=district)
        except SchoolDetail.DoesNotExist:
            # Create School object if it doesn't exist
            school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
            school_obj.save()


        # Step 2: Create Student Table (Foreign Key on School)
        student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob_formatted, student_class=student_class)
        student_obj.save()

        # Step 3: Create Student Marks Table
        marks_obj = StudentMark(student=student_obj, hindi=hindi, english=english, maths=maths, sanskrit=sanskrit, environmental_studies=environmental_studies, work_education=work_education, physical=physical, arts=arts)
        marks_obj.save()

        # Step 4: Create Marksheet Table (Foreign Key on Student and StudentMark)
        marksheet_obj = Marksheet(student=student_obj, marks=marks_obj, marksheet_id=marksheet_id, total_grade=total_grade, examination_date=exam_date_formatted)
        marksheet_obj.report_card.name = pdf_file_path
        marksheet_obj.save()


def process_marksheet_2(data):
    rows = data.shape[0]
    for row in range(rows):
        # Fetch Individual Student Data
        scholar_no = int(data.loc[row, 'scholar_no'])
        roll_no = int(data.loc[row, 'roll_no'])
        student_name = data.loc[row, 'student_name']
        father_name = data.loc[row, 'father_name']
        mother_name = data.loc[row, 'mother_name']
        dob = data.loc[row, 'dob']
        student_class = data.loc[row, 'student_class']
        school_name = data.loc[row, 'school_name']
        district = data.loc[row, 'district']
        block = data.loc[row, 'block']
        school_dice_code = int(data.loc[row, 'school_dice_code'])
        examination_center_code = int(data.loc[row, 'examination_center_code'])
        marksheet_id = int(data.loc[row, 'marksheet_id'])
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

        dob_datetime = parser.parse(dob)
        dob_formatted = dob_datetime.strftime('%Y-%m-%d')

        exam_date_datetime = parser.parse(examination_date)
        exam_date_formatted = exam_date_datetime.strftime('%Y-%m-%d')

        # Generate our Marksheet
        output_file_name = annotatePDF_format2(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # *** Add Details in Database ***
        # Step 1: Create School Table
        # NOTE: Check if school with the same details already exists
        school_obj = None
        try:
            school_obj = SchoolDetail.objects.get(school_name=school_name, district=district)
        except SchoolDetail.DoesNotExist:
            # Create School object if it doesn't exist
            school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
            school_obj.save()


        # Step 2: Create Student Table (Foreign Key on School)
        student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob_formatted, student_class=student_class)
        student_obj.save()

        # Step 3: Create Student Marks Table
        marks_obj = StudentMark(student=student_obj, hindi=hindi, english=english, maths=maths, sanskrit=sanskrit, science=science, social_science=social_science, work_education=work_education, physical=physical, arts=arts)
        marks_obj.save()

        # Step 4: Create Marksheet Table (Foreign Key on Student and StudentMark)
        marksheet_obj = Marksheet(student=student_obj, marks=marks_obj, marksheet_id=marksheet_id, total_grade=total_grade, examination_date=exam_date_formatted)
        marksheet_obj.report_card.name = pdf_file_path
        marksheet_obj.save()


def process_marksheet_3(data):
    rows = data.shape[0]
    for row in range(rows):
        # Fetch Individual Student Data
        scholar_no = int(data.loc[row, 'scholar_no'])
        roll_no = int(data.loc[row, 'roll_no'])
        student_name = data.loc[row, 'student_name']
        father_name = data.loc[row, 'father_name']
        mother_name = data.loc[row, 'mother_name']
        dob = data.loc[row, 'dob']
        swayam_pathi = data.loc[row, 'swayam_pathi']
        student_class = data.loc[row, 'student_class']
        school_name = data.loc[row, 'school_name']
        district = data.loc[row, 'district']
        block = data.loc[row, 'block']
        school_dice_code = int(data.loc[row, 'school_dice_code'])
        examination_center_code = int(data.loc[row, 'examination_center_code'])
        marksheet_id = int(data.loc[row, 'marksheet_id'])
        examination_date = data.loc[row, 'examination_date']
        result = data.loc[row, 'result']
        shreni = data.loc[row, 'shreni']
        percentage = data.loc[row, 'percentage']
        hindi_20 = int(data.loc[row, 'hindi_20'])
        hindi_80 = int(data.loc[row, 'hindi_80'])
        hindi_100 = int(data.loc[row, 'hindi_100'])
        english_20 = int(data.loc[row, 'english_20'])
        english_80 = int(data.loc[row, 'english_80'])
        english_100 = int(data.loc[row, 'english_100'])
        maths_20 = int(data.loc[row, 'maths_20'])
        maths_80 = int(data.loc[row, 'maths_80'])
        maths_100 = int(data.loc[row, 'maths_100'])
        science_20 = int(data.loc[row, 'science_20'])
        science_80 = int(data.loc[row, 'science_80'])
        science_100 = int(data.loc[row, 'science_100'])
        sanskrit_20 = int(data.loc[row, 'sanskrit_20'])
        sanskrit_80 = int(data.loc[row, 'sanskrit_80'])
        sanskrit_100 = int(data.loc[row, 'sanskrit_100'])
        social_science_20 = int(data.loc[row, 'social_science_20'])
        social_science_80 = int(data.loc[row, 'social_science_80'])
        social_science_100 = int(data.loc[row, 'social_science_100'])
        work_education_20 = int(data.loc[row, 'work_education_20'])
        work_education_80 = int(data.loc[row, 'work_education_80'])
        work_education_100 = int(data.loc[row, 'work_education_100'])
        arts_20 = int(data.loc[row, 'arts_20'])
        arts_80 = int(data.loc[row, 'arts_80'])
        arts_100 = int(data.loc[row, 'arts_100'])
        physical_20 = int(data.loc[row, 'physical_20'])
        physical_80 = int(data.loc[row, 'physical_80'])
        physical_100 = int(data.loc[row, 'physical_100'])


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

        dob_obj = datetime.strptime(dob, '%d-%m-%Y')
        dob_formatted = dob_obj.strftime('%Y-%m-%d')

        exam_date_datetime = datetime.strptime(dob, '%d-%m-%Y')
        exam_date_formatted = exam_date_datetime.strftime('%Y-%m-%d')

        # Generate our Marksheet
        output_file_name = annotatePDF_format3(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # *** Add Details in Database ***
        # Step 1: Create School Table
        school_obj = None
        try:
            school_obj = SchoolDetail.objects.get(school_name=school_name, district=district)
        except SchoolDetail.DoesNotExist:
            school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
            school_obj.save()

        # Step 2: Create Student Table (Foreign Key on School)
        student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob_formatted, student_class=student_class)
        student_obj.save()

        # Step 3: Create Student Marks Table
        marks_obj = StudentMark(student=student_obj, hindi_20 = hindi_20, hindi_80 = hindi_80, hindi_100 = hindi_100, english_20 = english_20, english_80 = english_80, english_100 = english_100, maths_20 = maths_20, maths_80 = maths_80, maths_100 = maths_100, science_20 = science_20, science_80 = science_80, science_100 = science_100, sanskrit_20 = sanskrit_20, sanskrit_80 = sanskrit_80, sanskrit_100 = sanskrit_100, social_science_20 = social_science_20, social_science_80 = social_science_80, social_science_100 = social_science_100, work_education_20 = work_education_20, work_education_80 = work_education_80, work_education_100 = work_education_100, arts_20 = arts_20, arts_80 = arts_80, arts_100 = arts_100, physical_20 = physical_20, physical_80 = physical_80, physical_100 = physical_100)
        marks_obj.save()

        # Step 4: Create Marksheet Table (Foreign Key on Student and StudentMark)
        marksheet_obj = Marksheet(student=student_obj, marks=marks_obj, marksheet_id=marksheet_id, result=result, shreni=shreni, percentage=percentage, examination_date=exam_date_formatted)
        marksheet_obj.report_card.name = pdf_file_path
        marksheet_obj.save()




def index(request):
    return render(request, "mainApp/index.html")

    # all_marksheets = Marksheet.objects.all()
    # paginator = Paginator(all_marksheets, 10)
    # page_number = request.GET.get("page")
    # data = paginator.get_page(page_number)
    # params = {'details': data}



def search(request):
    query = request.GET.get('search')
    params = {}
    if query:
        results = Marksheet.objects.filter(
            Q(student__scholar_no=query) |
            Q(student__roll_no=query) |
            Q(student__school__school_dice_code=query) |
            Q(student__student_name__icontains=query) |
            Q(student__school__school_name__icontains=query)
        )
        params['details'] = results
    else:
        results = Marksheet.objects.all()
        params['details'] = results

    return render(request, "index.html", params)


def about(request):
    return render(request, "mainApp/about.html")


def contact(request):
    return render(request, "mainApp/contact.html")


def upload(request):
    return render(request, "mainApp/data-upload.html")


def bulk_upload(request):
    if request.method == "POST" and request.FILES['csv_file']:
        selected_format = request.POST.get("print_format")
        csv_file = request.FILES['csv_file']
        data = pd.read_csv(csv_file)
        data.dropna(how='all', inplace=True)    # drop rows that have all empty values.

        if selected_format == "format_1":
            process_marksheet_1(data)

        elif selected_format == "format_2":
            process_marksheet_2(data)

        elif selected_format == "format_3":
            process_marksheet_3(data)

        return redirect('/bulk_upload')

    return render(request, "mainApp/bulk-data-upload.html")


def saveIndividualFormat1(request):
    scholar_no = request.POST.get('scholar_no')
    roll_no = request.POST.get('roll_no')
    student_name = request.POST.get('student_name')
    father_name = request.POST.get('father_name')
    mother_name = request.POST.get('mother_name')
    dob = request.POST.get('dob')

    student_class = request.POST.get('student_class')
    school_name = request.POST.get('school_name')
    district = request.POST.get('district')
    block = request.POST.get('block')
    school_dice_code = request.POST.get('school_dice_code')
    examination_center_code = request.POST.get('examination_center_code')

    marksheet_id = request.POST.get('marksheet_id')
    total_grade = request.POST.get('total_grade')
    examination_date = request.POST.get('examination_date')
    hindi = request.POST.get('hindi')
    english = request.POST.get('english')
    maths = request.POST.get('maths')
    sanskrit = request.POST.get('sanskrit')
    environmental_studies = request.POST.get('environmental_studies')
    work_education = request.POST.get('work_education')
    physical = request.POST.get('physical')
    arts = request.POST.get('arts')

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

    output_file_name = annotatePDF(report_data)
    pdf_file_path = os.path.join('pdf_files', output_file_name)

    school_obj = None
    try:
        school_obj = SchoolDetail.objects.get(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
    except SchoolDetail.DoesNotExist:
        school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
        school_obj.save()

    student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob, student_class=student_class)
    student_obj.save()

    marks_obj = StudentMark(student=student_obj, hindi=hindi, english=english, maths=maths, sanskrit=sanskrit, environmental_studies=environmental_studies, work_education=work_education, physical=physical, arts=arts)
    marks_obj.save()

    marksheet_obj = Marksheet(student=student_obj, marks=marks_obj, marksheet_id=marksheet_id, total_grade=total_grade, examination_date=examination_date)
    marksheet_obj.report_card.name = pdf_file_path
    marksheet_obj.save()


def saveIndividualFormat2(request):
    scholar_no = request.POST.get('scholar_no')
    roll_no = request.POST.get('roll_no')
    student_name = request.POST.get('student_name')
    father_name = request.POST.get('father_name')
    mother_name = request.POST.get('mother_name')
    dob = request.POST.get('dob')
    student_class = request.POST.get('student_class')
    school_name = request.POST.get('school_name')
    district = request.POST.get('district')
    block = request.POST.get('block')
    school_dice_code = request.POST.get('school_dice_code')
    examination_center_code = request.POST.get('examination_center_code')
    marksheet_id = request.POST.get('marksheet_id')
    total_grade = request.POST.get('total_grade')
    examination_date = request.POST.get('examination_date')
    hindi = request.POST.get('hindi')
    english = request.POST.get('english')
    maths = request.POST.get('maths')
    sanskrit = request.POST.get('sanskrit')
    science = request.POST.get('science')
    social_science = request.POST.get('social_science')
    work_education = request.POST.get('work_education')
    physical = request.POST.get('physical')
    arts = request.POST.get('arts')

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

    output_file_name = annotatePDF_format2(report_data)
    pdf_file_path = os.path.join('pdf_files', output_file_name)

    school_obj = None
    try:
        school_obj = SchoolDetail.objects.get(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
    except SchoolDetail.DoesNotExist:
        school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
        school_obj.save()

    student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob, student_class=student_class)
    student_obj.save()

    marks_obj = StudentMark(student=student_obj, hindi=hindi, english=english, maths=maths, sanskrit=sanskrit, science=science, social_science=social_science, work_education=work_education, physical=physical, arts=arts)
    marks_obj.save()

    marksheet_obj = Marksheet(student=student_obj, marks=marks_obj, marksheet_id=marksheet_id, total_grade=total_grade, examination_date=examination_date)
    marksheet_obj.report_card.name = pdf_file_path
    marksheet_obj.save()


def saveIndividualFormat3(request):
        scholar_no = request.POST.get('scholar_no')
        roll_no = request.POST.get('roll_no')
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        dob = request.POST.get('dob')

        swayam_pathi = request.POST.get('swayam_pathi')
        student_class = request.POST.get('student_class')
        school_name = request.POST.get('school_name')
        district = request.POST.get('district')
        block = request.POST.get('block')
        school_dice_code = request.POST.get('school_dice_code')
        examination_center_code = request.POST.get('examination_center_code')
        examination_date = request.POST.get('examination_date')

        result = request.POST.get('result')
        marksheet_id = request.POST.get('old_marksheet_id')
        shreni = request.POST.get('shreni')
        percentage = request.POST.get('percentage')
        hindi_20 = request.POST.get('hindi_20')
        hindi_80 = request.POST.get('hindi_80')
        hindi_100 = request.POST.get('hindi_100')
        english_20 = request.POST.get('english_20')
        english_80 = request.POST.get('english_80')
        english_100 = request.POST.get('english_100')
        maths_20 = request.POST.get('maths_20')
        maths_80 = request.POST.get('maths_80')
        maths_100 = request.POST.get('maths_100')
        science_20 = request.POST.get('science_20')
        science_80 = request.POST.get('science_80')
        science_100 = request.POST.get('science_100')
        sanskrit_20 = request.POST.get('sanskrit_20')
        sanskrit_80 = request.POST.get('sanskrit_80')
        sanskrit_100 = request.POST.get('sanskrit_100')
        social_science_20 = request.POST.get('social_science_20')
        social_science_80 = request.POST.get('social_science_80')
        social_science_100 = request.POST.get('social_science_100')
        work_education_20 = request.POST.get('work_education_20')
        work_education_80 = request.POST.get('work_education_80')
        work_education_100 = request.POST.get('work_education_100')
        arts_20 = request.POST.get('arts_20')
        arts_80 = request.POST.get('arts_80')
        arts_100 = request.POST.get('arts_100')
        physical_20 = request.POST.get('physical_20')
        physical_80 = request.POST.get('physical_80')
        physical_100 = request.POST.get('physical_100')


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

        output_file_name = annotatePDF_format3(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)

        school_obj = None
        try:
            school_obj = SchoolDetail.objects.get(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
        except SchoolDetail.DoesNotExist:
            school_obj = SchoolDetail(school_name=school_name, district=district, block=block, examination_center_code=examination_center_code, school_dice_code=school_dice_code)
            school_obj.save()

        student_obj = StudentDetail(school=school_obj, scholar_no=scholar_no, roll_no=roll_no, student_name=student_name, father_name=father_name, mother_name=mother_name, dob=dob, student_class=student_class)
        student_obj.save()

        marks_obj = StudentMark(student=student_obj, hindi_20 = hindi_20, hindi_80 = hindi_80, hindi_100 = hindi_100, english_20 = english_20, english_80 = english_80, english_100 = english_100, maths_20 = maths_20, maths_80 = maths_80, maths_100 = maths_100, science_20 = science_20, science_80 = science_80, science_100 = science_100, sanskrit_20 = sanskrit_20, sanskrit_80 = sanskrit_80, sanskrit_100 = sanskrit_100, social_science_20 = social_science_20, social_science_80 = social_science_80, social_science_100 = social_science_100, work_education_20 = work_education_20, work_education_80 = work_education_80, work_education_100 = work_education_100, arts_20 = arts_20, arts_80 = arts_80, arts_100 = arts_100, physical_20 = physical_20, physical_80 = physical_80, physical_100 = physical_100)
        marks_obj.save()

        marksheet_obj = Marksheet(student=student_obj, marks=marks_obj, marksheet_id=marksheet_id, result=result, shreni=shreni, percentage=percentage, examination_date=examination_date)
        marksheet_obj.report_card.name = pdf_file_path
        marksheet_obj.save()


def individual_upload(request):
    if request.method == "POST":
        marksheet_format = request.POST.get('marksheet_format')

        if marksheet_format == "1":
            saveIndividualFormat1(request)

        if marksheet_format == "2":
            saveIndividualFormat2(request)

        if marksheet_format == "3":
            saveIndividualFormat3(request)

    return render(request, "mainApp/individual_data_entry.html")


