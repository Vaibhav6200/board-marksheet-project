# -*- coding: utf-8 -*-
from pdf_annotate import PdfAnnotator, Appearance, Location
from django.conf import settings
import os
from datetime import datetime
from num2words import num2words
from translate import Translator


# def translate_text(text):
#     translator = Translator(to_lang="hi")  # Target language: Hindi
#     translation = translator.translate(text)
#     return translation


hex_color = "#696083"
fill_color = (0.412, 0.376, 0.514)


def convert_date_in_words(date_string):
    date_parts = date_string.split("-")
    day = num2words(int(date_parts[2]))
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    month = date_object.strftime("%B").lower()
    year = num2words(int(date_parts[0]))
    date = f"{day} {month} {year}"
    return date


def annotatePDF(data):
    base_dir = settings.BASE_DIR
    path = os.path.join(base_dir, 'media')
    template = os.path.join(path, 'marksheet_format_1.pdf')
    annotator = PdfAnnotator(template)

    # ***** Top Left Annotations *****
    # Praman Patra Kramank
    annotator.add_annotation(
                'text',
                    Location(x1=450, y1=805, x2=550, y2=825, page=0),
                    Appearance(content=data['marksheet_id'], font_size=10,  fill=fill_color),
                    )
    # School Name
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=675, x2=550, y2=700, page=0),
                    Appearance(content=data['school_name'], font_size=10,  fill=fill_color),
                    )
    # vidhyalaya praveshank
    annotator.add_annotation(
                'text',
                    Location(x1=40, y1=635, x2=130, y2=650, page=0),
                    Appearance(content=data['scholar_no'], font_size=10,  fill=fill_color),
                    )
    # Namank
    annotator.add_annotation(
                'text',
                    Location(x1=165, y1=635, x2=230, y2=650, page=0),
                    Appearance(content=data['roll_no'], font_size=10,  fill=fill_color),
                    )
    # Block
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=638, x2=330, y2=650, page=0),
                    Appearance(content=data['block'], font_size=10,  fill=fill_color),
                    )
    # district
    annotator.add_annotation(
                'text',
                    Location(x1=345, y1=638, x2=420, y2=650, page=0),
                    Appearance(content=data['district'], font_size=10,  fill=fill_color),
                    )
    # Dice Code
    annotator.add_annotation(
                'text',
                    Location(x1=450, y1=635, x2=540, y2=650, page=0),
                    Appearance(content=data['school_dice_code'], font_size=10,  fill=fill_color),
                    )

    # # jeela vidhalaya ki stithi mein namayata kramank
    # annotator.add_annotation(
    #             'text',
    #                 Location(x1=210, y1=610, x2=540, y2=625, page=0),
    #                 Appearance(content="This is a 43 characters long string ....................", font_size=10,  fill=fill_color),
    #             )

    # Students Name
    student_name = data['student_name']
    annotator.add_annotation(
                'text',
                    Location(x1=210, y1=585, x2=350, y2=600, page=0),
                    Appearance(content=student_name, font_size=10,  fill=fill_color),
                    )
    # Mothers Name
    annotator.add_annotation(
                'text',
                    Location(x1=410, y1=588, x2=550, y2=603, page=0),
                    Appearance(content=data['mother_name'], font_size=10,  fill=fill_color),
                    )

    # Fathers Name
    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=560, x2=200, y2=575, page=0),
                    Appearance(content=data['father_name'], font_size=10,  fill=fill_color),
                    )
    # Date of Birth
    annotator.add_annotation(
                'text',
                    Location(x1=370, y1=560, x2=500, y2=575, page=0),
                    Appearance(content=data['dob'], font_size=10,  fill=fill_color),
                    )
    # Date of Birth (in words)

    date_string = data['dob']
    date_in_english_words = convert_date_in_words(date_string)
    # date_in_hindi = translate_text(date_in_english_words)

    annotator.add_annotation(
                'text',
                    Location(x1=80, y1=533, x2=500, y2=548, page=0),
                    Appearance(content=date_in_english_words, font_size=10,  fill=fill_color),
                    )

    # ***** Grades Annotations *****
    # Hindi
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=450, x2=450, y2=470, page=0),
                    Appearance(content=str(data['hindi']), font_size=10,  fill=fill_color),
                    )
    # English
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=405, x2=450, y2=425, page=0),
                    Appearance(content=str(data['english']), font_size=10,  fill=fill_color),
                    )
    # Maths
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=360, x2=450, y2=380, page=0),
                    Appearance(content=str(data['maths']), font_size=10,  fill=fill_color),
                    )
    # Environmental Studies
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=310, x2=450, y2=330, page=0),
                    Appearance(content=str(data['environmental_studies']), font_size=10,  fill=fill_color),
                    )
    # Sanskrit / Urdu
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=260, x2=450, y2=280, page=0),
                    Appearance(content=str(data['sanskrit']), font_size=10,  fill=fill_color),
                    )
    # Arts
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=180, x2=450, y2=200, page=0),
                    Appearance(content=str(data['arts']), font_size=10,  fill=fill_color),
                    )
    # Work Education (Experience)
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=145, x2=450, y2=165, page=0),
                    Appearance(content=str(data['work_education']), font_size=10,  fill=fill_color),
                    )
    # Physical Education
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=105, x2=450, y2=125, page=0),
                    Appearance(content=str(data['physical']), font_size=10,  fill=fill_color),
                    )
    # Overall Grade
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=220, x2=450, y2=240, page=0),
                    Appearance(content=str(data['overall_grade']), font_size=10,  fill=fill_color),
                    )

    # ***** Bottom Left Annotations *****
    # Place
    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=60, x2=200, y2=75, page=0),
                    Appearance(content="Chittorgarh", font_size=10,  fill=fill_color),
                    )

    # Current Date
    now = datetime.now()
    formatted_date = now.strftime("%d-%b-%Y").lower()

    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=33, x2=400, y2=48, page=0),
                    Appearance(content=formatted_date, font_size=10,  fill=fill_color),
                )


    output_file_name = data['roll_no'] + "_" + data['student_name'] + '_format1.pdf'



    # Generate our Report card here
    path = os.path.join(base_dir, 'media')
    new_path = os.path.join(path, 'pdf_files')
    pdf_file_path = os.path.join(new_path, output_file_name)

    annotator.write(pdf_file_path, overwrite=True)

    return output_file_name

