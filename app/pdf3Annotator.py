from pdf_annotate import PdfAnnotator, Appearance, Location
from django.conf import settings
import os
from datetime import datetime
from num2words import num2words
from translate import Translator


def translate_text(text):
    translator = Translator(to_lang="hi")  # Target language: Hindi
    translation = translator.translate(text)
    return translation


fill_color = (0.514, 0.51, 0.635)

def convert_date_in_words(date_string):
    date_parts = date_string.split("-")
    day = num2words(int(date_parts[2]))
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    month = date_object.strftime("%B").lower()
    year = num2words(int(date_parts[0]))
    date = f"{day} {month} {year}"
    return date



def annotatePDF_format3(data):
    base_dir = settings.BASE_DIR
    path = os.path.join(base_dir, 'media')
    template = os.path.join(path, 'marksheet_format_3.pdf')
    annotator = PdfAnnotator(template)

    # Praman Patra Kramank
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=808, x2=170, y2=820, page=0),
                    Appearance(content=data['marksheet_id'], font_size=10,  fill=fill_color),
                    )

    # Namank (roll_no)
    annotator.add_annotation(
                'text',
                    Location(x1=80, y1=625, x2=150, y2=637, page=0),
                    Appearance(content=data['roll_no'], font_size=10,  fill=fill_color),
                    )

    # Scholar No
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=625, x2=220, y2=637, page=0),
                    Appearance(content=data['scholar_no'], font_size=10,  fill=fill_color),
                    )

    # swayam_pathi
    annotator.add_annotation(
                'text',
                    Location(x1=230, y1=625, x2=310, y2=637, page=0),
                    Appearance(content=data['swayam_pathi'], font_size=10,  fill=fill_color),
                    )

    # kendra (district)
    annotator.add_annotation(
                'text',
                    Location(x1=320, y1=625, x2=500, y2=637, page=0),
                    Appearance(content=data['district'], font_size=10,  fill=fill_color),
                    )

    # Student Name
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=602, x2=500, y2=614, page=0),
                    Appearance(content=data['student_name'], font_size=10,  fill=fill_color),
                    )

    # Father Name
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=580, x2=500, y2=592, page=0),
                    Appearance(content=data['father_name'], font_size=10,  fill=fill_color),
                    )

    # Mother Name
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=555, x2=500, y2=567, page=0),
                    Appearance(content=data['mother_name'], font_size=10,  fill=fill_color),
                    )

    # Date of Birth
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=530, x2=500, y2=542, page=0),
                    Appearance(content=data['dob'], font_size=10,  fill=fill_color),
                    )

    # Date of Birth in words
    date_string = data['dob']
    date_in_english_words = convert_date_in_words(date_string)
    # date_in_hindi = translate_text(date_in_english_words)

    annotator.add_annotation(
                'text',
                    Location(x1=130, y1=505, x2=500, y2=517, page=0),
                    Appearance(content=date_in_english_words, font_size=10,  fill=fill_color),
                    )

    # School Name
    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=465, x2=500, y2=477, page=0),
                    Appearance(content=data['school_name'], font_size=10,  fill=fill_color),
                    )

    # *** ENTER MARKS ***
    # Subject - Hindi_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=385, x2=450, y2=397, page=0),
                    Appearance(content=str(data['hindi_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - Hindi_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=385, x2=480, y2=397, page=0),
                    Appearance(content=str(data['hindi_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - Hindi_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=385, x2=530, y2=397, page=0),
                    Appearance(content=str(data['hindi_100']), font_size=10,  fill=fill_color),
                    )

    # Subject - English_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=360, x2=450, y2=372, page=0),
                    Appearance(content=str(data['english_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - English_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=360, x2=480, y2=372, page=0),
                    Appearance(content=str(data['english_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - English_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=360, x2=530, y2=372, page=0),
                    Appearance(content=str(data['english_100']), font_size=10,  fill=fill_color),
                    )

    # Subject - Maths_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=337, x2=450, y2=349, page=0),
                    Appearance(content=str(data['maths_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - Maths_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=337, x2=480, y2=349, page=0),
                    Appearance(content=str(data['maths_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - Maths_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=337, x2=530, y2=349, page=0),
                    Appearance(content=str(data['maths_100']), font_size=10,  fill=fill_color),
                    )

    # Subject - Science_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=313, x2=450, y2=325, page=0),
                    Appearance(content=str(data['science_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - Science_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=313, x2=480, y2=325, page=0),
                    Appearance(content=str(data['science_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - Science_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=313, x2=530, y2=325, page=0),
                    Appearance(content=str(data['science_100']), font_size=10,  fill=fill_color),
                    )

# Add extra Subject
    # Subject - sanskrit_urdu_100
    # Annotate Extra Subject name
    extra_subject_name = "Sanskrit / Urdu"
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=265, x2=450, y2=277, page=0),
                    Appearance(content=extra_subject_name, font_size=10,  fill=fill_color),
                    )

    # Subject - sanskrit_urdu_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=265, x2=450, y2=277, page=0),
                    Appearance(content=str(data['sanskrit_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - sanskrit_urdu_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=265, x2=480, y2=277, page=0),
                    Appearance(content=str(data['sanskrit_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - sanskrit_urdu_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=265, x2=530, y2=277, page=0),
                    Appearance(content=str(data['sanskrit_100']), font_size=10,  fill=fill_color),
                    )



    # Subject - Social Science_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=290, x2=450, y2=302, page=0),
                    Appearance(content=str(data['social_science_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - Social Science_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=290, x2=480, y2=302, page=0),
                    Appearance(content=str(data['social_science_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - Social Science_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=290, x2=530, y2=302, page=0),
                    Appearance(content=str(data['social_science_100']), font_size=10,  fill=fill_color),
                    )

    # Subject - work_education_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=240, x2=450, y2=252, page=0),
                    Appearance(content=str(data['work_education_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - work_education_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=240, x2=480, y2=252, page=0),
                    Appearance(content=str(data['work_education_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - work_education_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=240, x2=530, y2=252, page=0),
                    Appearance(content=str(data['work_education_100']), font_size=10,  fill=fill_color),
                    )

    # Subject - arts_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=218, x2=450, y2=230, page=0),
                    Appearance(content=str(data['arts_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - arts_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=218, x2=480, y2=230, page=0),
                    Appearance(content=str(data['arts_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - arts_80
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=218, x2=530, y2=230, page=0),
                    Appearance(content=str(data['arts_100']), font_size=10,  fill=fill_color),
                    )

    # Subject - physical_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=193, x2=450, y2=205, page=0),
                    Appearance(content=str(data['physical_20']), font_size=10,  fill=fill_color),
                    )

    # Subject - physical_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=193, x2=480, y2=205, page=0),
                    Appearance(content=str(data['physical_80']), font_size=10,  fill=fill_color),
                    )

    # Subject - physical_80
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=193, x2=530, y2=205, page=0),
                    Appearance(content=str(data['physical_100']), font_size=10,  fill=fill_color),
                    )

    # percentage
    annotator.add_annotation(
                'text',
                    Location(x1=455, y1=170, x2=500, y2=182, page=0),
                    Appearance(content=str(data['percentage']), font_size=10,  fill=fill_color),
                    )

    # result
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=145, x2=170, y2=157, page=0),
                    Appearance(content=data['result'], font_size=10,  fill=fill_color),
                    )

    # shreni
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=146, x2=340, y2=158, page=0),
                    Appearance(content=data['shreni'], font_size=10,  fill=fill_color),
                    )

    # TODAY DATE (print current date)

    # Get current date
    now = datetime.now()
    formatted_date = now.strftime("%d-%b-%Y").lower()

    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=73, x2=350, y2=83, page=0),
                    Appearance(content=formatted_date, font_size=10,  fill=fill_color),
                    )


    output_file_name = data['roll_no'] + "_" + data['student_name'] + '_format3.pdf'


    # Generate our Report card here
    path = os.path.join(base_dir, 'media')
    new_path = os.path.join(path, 'pdf_files')
    pdf_file_path = os.path.join(new_path, output_file_name)
    annotator.write(pdf_file_path, overwrite=True)

    return output_file_name

