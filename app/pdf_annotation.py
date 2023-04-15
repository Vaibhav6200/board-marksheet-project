from pdf_annotate import PdfAnnotator, Appearance, Location
from datetime import datetime, date
from django.conf import settings
import os


def annotatePDF(data):
    base_dir = settings.BASE_DIR
    path = os.path.join(base_dir, 'media')
    template = os.path.join(path, 'DIET.pdf')
    annotator = PdfAnnotator(template)

    # ***** Top Left Annotations *****
    # Praman Patra Kramank
    annotator.add_annotation(
                'text',
                    Location(x1=450, y1=805, x2=550, y2=825, page=0),
                    Appearance(content=data['marksheet_id'], font_size=10,  fill=(0,0,0)),
                    )
    # School Name
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=675, x2=550, y2=700, page=0),
                    Appearance(content=data['school_name'], font_size=10,  fill=(0,0,0)),
                    )
    # vidhyalaya praveshank
    annotator.add_annotation(
                'text',
                    Location(x1=40, y1=635, x2=130, y2=650, page=0),
                    Appearance(content=data['scholar_no'], font_size=10,  fill=(0,0,0)),
                    )
    # Namank
    annotator.add_annotation(
                'text',
                    Location(x1=165, y1=635, x2=230, y2=650, page=0),
                    Appearance(content=data['roll_no'], font_size=10,  fill=(0,0,0)),
                    )
    # Block
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=638, x2=330, y2=650, page=0),
                    Appearance(content=data['block'], font_size=10,  fill=(0,0,0)),
                    )
    # district
    annotator.add_annotation(
                'text',
                    Location(x1=345, y1=638, x2=420, y2=650, page=0),
                    Appearance(content=data['district'], font_size=10,  fill=(0,0,0)),
                    )
    # Dice Code
    annotator.add_annotation(
                'text',
                    Location(x1=450, y1=635, x2=540, y2=650, page=0),
                    Appearance(content=data['school_dice_code'], font_size=10,  fill=(0,0,0)),
                    )

    # # jeela vidhalaya ki stithi mein namayata kramank
    # annotator.add_annotation(
    #             'text',
    #                 Location(x1=210, y1=610, x2=540, y2=625, page=0),
    #                 Appearance(content="This is a 43 characters long string ....................", font_size=10,  fill=(0,0,0)),
    #             )

    # Students Name
    annotator.add_annotation(
                'text',
                    Location(x1=210, y1=585, x2=350, y2=600, page=0),
                    Appearance(content=data['student_name'], font_size=10,  fill=(0,0,0)),
                    )
    # Mothers Name
    annotator.add_annotation(
                'text',
                    Location(x1=410, y1=588, x2=550, y2=603, page=0),
                    Appearance(content=data['mother_name'], font_size=10,  fill=(0,0,0)),
                    )

    # Fathers Name
    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=560, x2=200, y2=575, page=0),
                    Appearance(content=data['father_name'], font_size=10,  fill=(0,0,0)),
                    )
    # Date of Birth
    # dob = date(2002, 2, 22)
    # dob_string = dob.strftime('%d-%m-%Y')
    annotator.add_annotation(
                'text',
                    Location(x1=370, y1=560, x2=500, y2=575, page=0),
                    Appearance(content=data['dob'], font_size=10,  fill=(0,0,0)),
                    )
    # Date of Birth (in words)
    # dob_string_words = "twenty two february two thousand two"
    # annotator.add_annotation(
    #             'text',
    #                 Location(x1=80, y1=533, x2=500, y2=548, page=0),
    #                 Appearance(content=dob_string_words, font_size=10,  fill=(0,0,0)),
    #                 )

    # ***** Grades Annotations *****
    # Hindi
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=450, x2=450, y2=470, page=0),
                    Appearance(content=str(data['subject_1']), font_size=10,  fill=(0,0,0)),
                    )
    # English
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=405, x2=450, y2=425, page=0),
                    Appearance(content=str(data['subject_2']), font_size=10,  fill=(0,0,0)),
                    )
    # Maths
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=360, x2=450, y2=380, page=0),
                    Appearance(content=str(data['subject_3']), font_size=10,  fill=(0,0,0)),
                    )
    # Environment
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=310, x2=450, y2=330, page=0),
                    Appearance(content=str(data['subject_4']), font_size=10,  fill=(0,0,0)),
                    )
    # Sanskrit / Urdu
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=260, x2=450, y2=280, page=0),
                    Appearance(content=str(data['subject_5']), font_size=10,  fill=(0,0,0)),
                    )
    # creativity
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=180, x2=450, y2=200, page=0),
                    Appearance(content=str(data['subject_6']), font_size=10,  fill=(0,0,0)),
                    )
    # Experience
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=145, x2=450, y2=165, page=0),
                    Appearance(content=str(data['subject_7']), font_size=10,  fill=(0,0,0)),
                    )
    # Health
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=105, x2=450, y2=125, page=0),
                    Appearance(content=str(data['subject_8']), font_size=10,  fill=(0,0,0)),
                    )
    # Overall Grade
    annotator.add_annotation(
                'text',
                    Location(x1=430, y1=220, x2=450, y2=240, page=0),
                    Appearance(content=str(data['overall_grade']), font_size=10,  fill=(0,0,0)),
                    )

    # ***** Bottom Left Annotations *****
    # Place
    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=60, x2=200, y2=75, page=0),
                    Appearance(content=str(data['examination_center']), font_size=10,  fill=(0,0,0)),
                    )

    # Date
    # Get the current date and format it
    # now = datetime.now()
    # date_string = now.strftime('%d-%m-%Y')

    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=33, x2=400, y2=48, page=0),
                    Appearance(content=str(data['examination_date']), font_size=10,  fill=(0,0,0)),
                    )


    output_file_name = data['roll_no'] + '.pdf'


    # Generate our Report card here
    path = os.path.join(base_dir, 'media')
    new_path = os.path.join(path, 'pdf_files')
    pdf_file_path = os.path.join(new_path, output_file_name)

    annotator.write(pdf_file_path, overwrite=True)

    return output_file_name



