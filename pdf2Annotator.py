from pdf_annotate import PdfAnnotator, Appearance, Location


def annotatePDF_format2(data):
    annotator = PdfAnnotator('DIET1.pdf')

    # Praman Patra Kramank
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=750, x2=170, y2=760, page=0),
                    Appearance(content=data['marksheet_id'], font_size=10,  fill=(0,0,0)),
                    )


    # School Name
    annotator.add_annotation(
                'text',
                    Location(x1=190, y1=595, x2=500, y2=605, page=0),
                    Appearance(content=data['school_name'], font_size=10,  fill=(0,0,0)),
                    )

    # Scholar No
    annotator.add_annotation(
                'text',
                    Location(x1=125, y1=517, x2=180, y2=527, page=0),
                    Appearance(content=data['scholar_no'], font_size=10,  fill=(0,0,0)),
                    )

    # roll_no
    annotator.add_annotation(
                'text',
                    Location(x1=200, y1=517, x2=250, y2=527, page=0),
                    Appearance(content=data['roll_no'], font_size=10,  fill=(0,0,0)),
                    )

    # district
    annotator.add_annotation(
                'text',
                    Location(x1=260, y1=517, x2=320, y2=527, page=0),
                    Appearance(content=data['district'], font_size=10,  fill=(0,0,0)),
                    )

    # block
    annotator.add_annotation(
                'text',
                    Location(x1=340, y1=517, x2=370, y2=527, page=0),
                    Appearance(content=data['block'], font_size=10,  fill=(0,0,0)),
                    )

    # school_dice_code
    annotator.add_annotation(
                'text',
                    Location(x1=390, y1=517, x2=470, y2=527, page=0),
                    Appearance(content=data['school_dice_code'], font_size=10,  fill=(0,0,0)),
                    )

    # kendra_code
    annotator.add_annotation(
                'text',
                    Location(x1=480, y1=517, x2=530, y2=527, page=0),
                    Appearance(content=data['kendra_code'], font_size=10,  fill=(0,0,0)),
                    )


    # *** STUDENT DATA ***
    # student_name
    annotator.add_annotation(
                'text',
                    Location(x1=270, y1=497, x2=500, y2=507, page=0),
                    Appearance(content=data['student_name'], font_size=10,  fill=(0,0,0)),
                    )

    # mother_name
    annotator.add_annotation(
                'text',
                    Location(x1=170, y1=473, x2=300, y2=483, page=0),
                    Appearance(content=data['mother_name'], font_size=10,  fill=(0,0,0)),
                    )

    # father_name
    annotator.add_annotation(
                'text',
                    Location(x1=370, y1=473, x2=520, y2=483, page=0),
                    Appearance(content=data['father_name'], font_size=10,  fill=(0,0,0)),
                    )

    # dob
    annotator.add_annotation(
                'text',
                    Location(x1=200, y1=445, x2=300, y2=455, page=0),
                    Appearance(content=data['dob'], font_size=10,  fill=(0,0,0)),
                    )

    # dob in words
    dob_in_words="twenty two february two thousand two"
    annotator.add_annotation(
                'text',
                    Location(x1=320, y1=450, x2=520, y2=460, page=0),
                    Appearance(content=dob_in_words, font_size=10,  fill=(0,0,0)),
                    )

    # examination_year
    annotator.add_annotation(
                'text',
                    Location(x1=330, y1=425, x2=520, y2=435, page=0),
                    Appearance(content=data['examination_date'], font_size=10,  fill=(0,0,0)),
                    )

    # *** ENTER MARKS ***
    # Subject - Hindi
    annotator.add_annotation(
                'text',
                    Location(x1=485, y1=330, x2=510, y2=340, page=0),
                    Appearance(content=str(data['hindi']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - English
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=305, x2=510, y2=314, page=0),
                    Appearance(content=str(data['english']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Maths
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=279, x2=510, y2=289, page=0),
                    Appearance(content=str(data['maths']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Science
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=255, x2=510, y2=265, page=0),
                    Appearance(content=str(data['science']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - socialScience
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=230, x2=510, y2=240, page=0),
                    Appearance(content=str(data['social_science']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - tritiya_bhasha
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=205, x2=510, y2=215, page=0),
                    Appearance(content=str(data['tritiya_bhasha']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Overall Grade
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=182, x2=510, y2=192, page=0),
                    Appearance(content=str(data['overall_grade']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - experience
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=163, x2=510, y2=173, page=0),
                    Appearance(content=str(data['experience']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - creativity
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=138, x2=510, y2=148, page=0),
                    Appearance(content=str(data['creativity']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - health
    annotator.add_annotation(
                'text',
                    Location(x1=484, y1=115, x2=510, y2=125, page=0),
                    Appearance(content=str(data['health']), font_size=10,  fill=(0,0,0)),
                    )



    # Examination Center
    annotator.add_annotation(
                'text',
                    Location(x1=155, y1=65, x2=500, y2=75, page=0),
                    Appearance(content=data['examination_center'], font_size=10,  fill=(0,0,0)),
                    )

    # Examination Date
    annotator.add_annotation(
                'text',
                    Location(x1=155, y1=43, x2=350, y2=53, page=0),
                    Appearance(content=data['examination_date'], font_size=10,  fill=(0,0,0)),
                    )


    annotator.write("output_2.pdf", overwrite=True)



data = {
    "marksheet_id":"1122334455",
    "school_name": "St. Paul's Sr. Sec. School",
    "scholar_no": "20bce308",
    "roll_no": "1104563",
    "district": "Chittorgarh",
    "block": "A",
    "school_dice_code": "1032",
    "kendra_code": "390474",
    "student_name": "vaibhav paliwal",
    "father_name": "gopal paliwal",
    "mother_name": "sharda paliwal",
    "dob": "22-02-2002",
    "hindi": "A",
    "english": "B",
    "maths": "A+",
    "science": "A",
    "social_science": "C",
    "tritiya_bhasha": "B",
    "experience": "A+",
    "creativity": "A+",
    "health": "B",
    "overall_grade": "A",
    "examination_center": "Delhi Public school, Udaipur",
    "examination_date": "29-march-2020",
}

annotatePDF_format2(data)