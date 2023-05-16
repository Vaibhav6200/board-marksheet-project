from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
from .models import *
from .pdf_annotation import annotatePDF
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
        exam_date_formatted = dob_datetime.strftime('%Y-%m-%d')


        # Generate our Marksheet
        output_file_name = annotatePDF(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # *** Add Details in Database ***
        # Step 1: Create School Table
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
    pass

def process_marksheet_3(data):
    pass


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
    details = MarksheetFormat_1.objects.all()
    params = {'details': details}


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




