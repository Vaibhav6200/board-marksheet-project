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


def getGrade(marks):
    if marks>=91 and marks<=100:
        return "A+"
    elif marks>=76 and marks<=90:
        return "A"
    elif marks>=61 and marks<=75:
        return "B"
    elif marks>=41 and marks<=60:
        return "C"
    else:
        return "D"


def process_data(data):
    for student in data.values:

        exam_date = student[13]
        date_obj = datetime.strptime(exam_date, "%d-%b-%y")
        formatted_exam_date = date_obj.strftime("%Y-%m-%d")

        dob_date = student[5]
        dob_obj = datetime.strptime(dob_date, "%d-%b-%y")
        formatted_dob = dob_obj.strftime("%Y-%m-%d")


        sub9_marks = 0.0
        average_marks = 0.0
        student_class = student[6]
        if student_class == 8:
            sub9_marks = student[22]        # Explicitly taking values of subject 9 cause its Not Appilcable for class 5 students
            average_marks = (sum(student[14:22]) + sub9_marks) / 9
        else:
            average_marks = sum(student[14:22]) / 8.0

        overall_grade = getGrade(average_marks)


        report_data = {
            'scholar_no': str(student[0]),
            'roll_no': str(student[1]),
            'student_name': student[2],
            'father_name': student[3],
            'mother_name': student[4],
            'dob': dob_date,
            'student_class': student[6],
            'school_name': student[7],
            'block': student[8],
            'district': student[9],
            'school_dice_code': str(student[10]),
            'examination_center': student[11],
            'examination_center_code': student[12],
            'examination_date': exam_date,
            'subject_1': getGrade(student[14]),
            'subject_2': getGrade(student[15]),
            'subject_3': getGrade(student[16]),
            'subject_4': getGrade(student[17]),
            'subject_5': getGrade(student[18]),
            'subject_6': getGrade(student[19]),
            'subject_7': getGrade(student[20]),
            'subject_8': getGrade(student[21]),
            'subject_9': getGrade(sub9_marks),
            'marksheet_id':str(student[23]),
            'average_marks': average_marks,
            'overall_grade': overall_grade
        }

        # Generate our Report card here
        output_file_name = annotatePDF(report_data)
        pdf_file_path = os.path.join('pdf_files', output_file_name)


        # Now Create Marksheet of our student
        # mymarksheet = MarksheetFormat_1(scholar_no =report_data['scholar_no'], roll_no = report_data['roll_no'], student_name=report_data['student_name'], father_name=report_data['father_name'], mother_name = report_data['mother_name'],
        #                          dob = formatted_dob,
        #                          examination_date = formatted_exam_date,
        #                          student_class = report_data['student_class'], school_name = report_data['school_name'], block = report_data['block'], district = report_data['district'], school_dice_code = report_data['school_dice_code'],
        #                          examination_center = report_data['examination_center'], examination_center_code = report_data['examination_center_code'],
        #                          subject_1 = student[14], subject_2 = student[15], subject_3 = student[16], subject_4 = student[17], subject_5 = student[18],
        #                          subject_6 = student[19], subject_7 = student[20], subject_8 = student[21], subject_9 = sub9_marks,
        #                          grade = report_data['overall_grade'], average = report_data['average_marks'], marksheet_id=report_data['marksheet_id'])

        # mymarksheet.save()
        # mymarksheet.report_card.name = pdf_file_path
        # mymarksheet.save()


def index(request):
    if request.method == "POST" and request.FILES['csv_file']:
        selected_format = request.POST.get("dropdown_button")

        # Marksheet format 1
        if selected_format == "format_1":
            csv_file = request.FILES['csv_file']
            data = pd.read_csv(csv_file)

            # Process Data (add all data to our database)
            process_data(data)

        # Marksheet Format 2
        elif selected_format == "format_2":
            pass

        # Marksheet Format 3
        elif selected_format == "format_3":
            pass


        # return redirect('/')        # this helps in prevention of form resubmission on reloading page

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