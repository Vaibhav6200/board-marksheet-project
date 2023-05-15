from pdf_annotate import PdfAnnotator, Appearance, Location
import datetime


hex_color = "#6471a6"
fill_color = (0.392, 0.443, 0.651)

def annotatePDF_format2(data):
    annotator = PdfAnnotator('marksheet_format_2.pdf')

    # Praman Patra Kramank
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=790, x2=270, y2=810, page=0),
                    Appearance(content=data['marksheet_id'], font_size=15, fill=fill_color),
                    )


    # SATRA (Examination date)
    satra = data['examination_year']
    annotator.add_annotation(
                'text',
                    Location(x1=280, y1=640, x2=500, y2=660, page=0),
                    Appearance(content=satra, font_size=15,  fill=fill_color),
                    )

    # School Name
    annotator.add_annotation(
                'text',
                    Location(x1=200, y1=620, x2=500, y2=632, page=0),
                    Appearance(content=data['school_name'], font_size=10,  fill=fill_color),
                    )

    # Scholar No
    annotator.add_annotation(
                'text',
                    Location(x1=105, y1=530, x2=180, y2=542, page=0),
                    Appearance(content=data['scholar_no'], font_size=10,  fill=fill_color),
                    )

    # roll_no
    annotator.add_annotation(
                'text',
                    Location(x1=180, y1=530, x2=250, y2=542, page=0),
                    Appearance(content=data['roll_no'], font_size=10,  fill=fill_color),
                    )

    # district
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=530, x2=320, y2=542, page=0),
                    Appearance(content=data['district'], font_size=10,  fill=fill_color),
                    )

    # block
    annotator.add_annotation(
                'text',
                    Location(x1=380, y1=530, x2=390, y2=542, page=0),
                    Appearance(content=data['block'], font_size=10,  fill=fill_color),
                    )

    # school_dice_code
    annotator.add_annotation(
                'text',
                    Location(x1=230, y1=597, x2=470, y2=610, page=0),
                    Appearance(content=data['school_dice_code'], font_size=10,  fill=fill_color),
                    )

    # kendra_code
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=530, x2=530, y2=542, page=0),
                    Appearance(content=data['kendra_code'], font_size=10,  fill=fill_color),
                    )


    # *** STUDENT DATA ***
    # student_name
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=510, x2=500, y2=522, page=0),
                    Appearance(content=data['student_name'], font_size=10,  fill=fill_color),
                    )

    # mother_name
    annotator.add_annotation(
                'text',
                    Location(x1=170, y1=485, x2=300, y2=497, page=0),
                    Appearance(content=data['mother_name'], font_size=10,  fill=fill_color),
                    )

    # father_name
    annotator.add_annotation(
                'text',
                    Location(x1=370, y1=485, x2=520, y2=497, page=0),
                    Appearance(content=data['father_name'], font_size=10,  fill=fill_color),
                    )

    # dob
    annotator.add_annotation(
                'text',
                    Location(x1=170, y1=457, x2=250, y2=470, page=0),
                    Appearance(content=data['dob'], font_size=10,  fill=fill_color),
                    )

    # dob in words
    dob_in_words="twenty two february two thousand two"
    annotator.add_annotation(
                'text',
                    Location(x1=320, y1=460, x2=520, y2=472, page=0),
                    Appearance(content=dob_in_words, font_size=10,  fill=fill_color),
                    )

    # examination_year
    annotator.add_annotation(
                'text',
                    Location(x1=310, y1=435, x2=520, y2=447, page=0),
                    Appearance(content=data['examination_year'], font_size=10,  fill=fill_color),
                    )

    # *** ENTER MARKS ***
    # Subject - HINDI
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=340, x2=480, y2=352, page=0),
                    Appearance(content=str(data['HINDI']), font_size=10,  fill=fill_color),
                    )

    # Subject - ENGLISH
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=315, x2=480, y2=327, page=0),
                    Appearance(content=str(data['ENGLISH']), font_size=10,  fill=fill_color),
                    )

    # Subject - MATHS
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=290, x2=480, y2=302, page=0),
                    Appearance(content=str(data['MATHS']), font_size=10,  fill=fill_color),
                    )

    # Subject - Science
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=265, x2=480, y2=277, page=0),
                    Appearance(content=str(data['SCIENCE']), font_size=10,  fill=fill_color),
                    )

    # Subject - socialScience
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=240, x2=480, y2=252, page=0),
                    Appearance(content=str(data['S.S']), font_size=10,  fill=fill_color),
                    )

    # Subject - SANSKRIT
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=215, x2=480, y2=227, page=0),
                    Appearance(content=str(data['SANSKRIT']), font_size=10,  fill=fill_color),
                    )

    # Subject - Overall Grade
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=195, x2=480, y2=207, page=0),
                    Appearance(content=str(data['GRADETOT']), font_size=10,  fill=fill_color),
                    )

    # Subject - W.E.
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=170, x2=480, y2=182, page=0),
                    Appearance(content=str(data['W.E.']), font_size=10,  fill=fill_color),
                    )

    # Subject - PHI.
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=145, x2=480, y2=157, page=0),
                    Appearance(content=str(data['PHI.']), font_size=10,  fill=fill_color),
                    )

    # Subject - ARTS
    annotator.add_annotation(
                'text',
                    Location(x1=460, y1=125, x2=480, y2=137, page=0),
                    Appearance(content=str(data['ARTS']), font_size=10,  fill=fill_color),
                    )



    # Examination Center
    exam_center = "Chittorgarh"
    annotator.add_annotation(
                'text',
                    Location(x1=130, y1=70, x2=500, y2=82, page=0),
                    Appearance(content=exam_center, font_size=10,  fill=fill_color),
                    )

    # Examination Date
    # Get current date
    now = datetime.datetime.now()
    formatted_date = now.strftime("%d-%b-%Y").lower()

    annotator.add_annotation(
                'text',
                    Location(x1=130, y1=45, x2=350, y2=57, page=0),
                    Appearance(content=formatted_date, font_size=10,  fill=fill_color),
                    )


    annotator.write("output_2.pdf", overwrite=True)



data = {
    "scholar_no": "20bce308",
    "roll_no": "1104563",
    "student_name": "student_name",
    "father_name": "father_name",
    "mother_name": "mother_name",
    "dob": "22-02-2002",
    # "student_class": "8",     # NOT USED
    "school_name": "St. Paul's Sr. Sec. School",
    "block": "A",
    "district": "Chittorgarh",
    "school_dice_code": "1032",

    # "examination_center": "Chittorgarh",  # NOT USED
    # "examination_center_code": "9001",    # NOT USED
    "examination_year": "2019 - 20",

    "HINDI": "A",
    "ENGLISH": "B",
    "SCIENCE": "A",
    "S.S": "C",     # Social Science
    "MATHS": "A+",
    "SANSKRIT": "B",
    "W.E.": "C",    # working education
    "PHI.": "A+",
    "ARTS": "A",
    "GRADETOT": "A",

    "marksheet_id":"1122334455",
    "kendra_code": "390474",
}

annotatePDF_format2(data)