from pdf_annotate import PdfAnnotator, Appearance, Location


def annotatePDF_format3(data):
    annotator = PdfAnnotator('DIET8.pdf')

    # Praman Patra Kramank
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=808, x2=170, y2=820, page=0),
                    Appearance(content=data['marksheet_id'], font_size=10,  fill=(0,0,0)),
                    )

    # Namank (roll_no)
    annotator.add_annotation(
                'text',
                    Location(x1=80, y1=625, x2=150, y2=635, page=0),
                    Appearance(content=data['roll_no'], font_size=10,  fill=(0,0,0)),
                    )

    # Scholar No
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=625, x2=220, y2=635, page=0),
                    Appearance(content=data['scholar_no'], font_size=10,  fill=(0,0,0)),
                    )

    # swayam_pathi
    annotator.add_annotation(
                'text',
                    Location(x1=240, y1=625, x2=300, y2=635, page=0),
                    Appearance(content=data['swayam_pathi'], font_size=10,  fill=(0,0,0)),
                    )

    # kendra (district)
    annotator.add_annotation(
                'text',
                    Location(x1=320, y1=625, x2=500, y2=635, page=0),
                    Appearance(content=data['district'], font_size=10,  fill=(0,0,0)),
                    )

    # Student Name
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=602, x2=500, y2=612, page=0),
                    Appearance(content=data['student_name'], font_size=10,  fill=(0,0,0)),
                    )

    # Father Name
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=580, x2=500, y2=590, page=0),
                    Appearance(content=data['father_name'], font_size=10,  fill=(0,0,0)),
                    )

    # Mother Name
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=555, x2=500, y2=565, page=0),
                    Appearance(content=data['mother_name'], font_size=10,  fill=(0,0,0)),
                    )

    # Date of Birth
    annotator.add_annotation(
                'text',
                    Location(x1=160, y1=530, x2=500, y2=540, page=0),
                    Appearance(content=data['dob'], font_size=10,  fill=(0,0,0)),
                    )

    # Date of Birth in words
    dob_in_words="twenty two february two thousand two"
    annotator.add_annotation(
                'text',
                    Location(x1=130, y1=505, x2=500, y2=515, page=0),
                    Appearance(content=dob_in_words, font_size=10,  fill=(0,0,0)),
                    )

    # School Name
    annotator.add_annotation(
                'text',
                    Location(x1=70, y1=465, x2=500, y2=475, page=0),
                    Appearance(content=data['school_name'], font_size=10,  fill=(0,0,0)),
                    )

    # *** ENTER MARKS ***
    # Subject - Hindi_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=385, x2=450, y2=395, page=0),
                    Appearance(content=str(data['hindi_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Hindi_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=385, x2=480, y2=395, page=0),
                    Appearance(content=str(data['hindi_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Hindi_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=385, x2=530, y2=395, page=0),
                    Appearance(content=str(data['hindi_100']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - English_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=360, x2=450, y2=370, page=0),
                    Appearance(content=str(data['english_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - English_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=360, x2=480, y2=370, page=0),
                    Appearance(content=str(data['english_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - English_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=360, x2=530, y2=370, page=0),
                    Appearance(content=str(data['english_100']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Maths_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=337, x2=450, y2=347, page=0),
                    Appearance(content=str(data['maths_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Maths_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=337, x2=480, y2=347, page=0),
                    Appearance(content=str(data['maths_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Maths_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=337, x2=530, y2=347, page=0),
                    Appearance(content=str(data['maths_100']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Science_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=313, x2=450, y2=323, page=0),
                    Appearance(content=str(data['science_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Science_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=313, x2=480, y2=323, page=0),
                    Appearance(content=str(data['science_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Science_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=313, x2=530, y2=323, page=0),
                    Appearance(content=str(data['science_100']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Social Science_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=290, x2=450, y2=300, page=0),
                    Appearance(content=str(data['social_science_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Social Science_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=290, x2=480, y2=300, page=0),
                    Appearance(content=str(data['social_science_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - Social Science_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=290, x2=530, y2=300, page=0),
                    Appearance(content=str(data['social_science_100']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - experience_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=240, x2=450, y2=250, page=0),
                    Appearance(content=str(data['experience_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - experience_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=240, x2=480, y2=250, page=0),
                    Appearance(content=str(data['experience_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - experience_100
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=240, x2=530, y2=250, page=0),
                    Appearance(content=str(data['experience_100']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - creativity_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=218, x2=450, y2=228, page=0),
                    Appearance(content=str(data['creativity_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - creativity_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=218, x2=480, y2=228, page=0),
                    Appearance(content=str(data['creativity_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - creativity_80
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=218, x2=530, y2=228, page=0),
                    Appearance(content=str(data['creativity_100']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - health_20
    annotator.add_annotation(
                'text',
                    Location(x1=423, y1=193, x2=450, y2=203, page=0),
                    Appearance(content=str(data['health_20']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - health_80
    annotator.add_annotation(
                'text',
                    Location(x1=465, y1=193, x2=480, y2=203, page=0),
                    Appearance(content=str(data['health_80']), font_size=10,  fill=(0,0,0)),
                    )

    # Subject - health_80
    annotator.add_annotation(
                'text',
                    Location(x1=510, y1=193, x2=530, y2=203, page=0),
                    Appearance(content=str(data['health_100']), font_size=10,  fill=(0,0,0)),
                    )

    # total_marks
    annotator.add_annotation(
                'text',
                    Location(x1=455, y1=170, x2=500, y2=180, page=0),
                    Appearance(content=str(data['total_marks']), font_size=10,  fill=(0,0,0)),
                    )

    # Parinaam
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=145, x2=170, y2=155, page=0),
                    Appearance(content=data['parinaam'], font_size=10,  fill=(0,0,0)),
                    )

    # shreni
    annotator.add_annotation(
                'text',
                    Location(x1=250, y1=146, x2=340, y2=156, page=0),
                    Appearance(content=data['shreni'], font_size=10,  fill=(0,0,0)),
                    )

    # variyata_kramank
    annotator.add_annotation(
                'text',
                    Location(x1=425, y1=145, x2=540, y2=155, page=0),
                    Appearance(content=data['variyata_kramank'], font_size=10,  fill=(0,0,0)),
                    )

    # Examination Center
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=98, x2=500, y2=108, page=0),
                    Appearance(content=data['examination_center'], font_size=10,  fill=(0,0,0)),
                    )

    # Examination Date
    annotator.add_annotation(
                'text',
                    Location(x1=110, y1=73, x2=350, y2=83, page=0),
                    Appearance(content=data['examination_date'], font_size=10,  fill=(0,0,0)),
                    )


    annotator.write("output_3.pdf", overwrite=True)



data = {
    "marksheet_id":"1122334455",
    "roll_no": "1104563",
    "scholar_no": "20bce308",
    "school_name": "St. Paul's Sr. Sec. School",
    "swayam_pathi": "Mukund",
    "district": "Chittorgarh",
    "student_name": "vaibhav paliwal",
    "father_name": "gopal paliwal",
    "mother_name": "sharda paliwal",
    "dob": "22-02-2002",
    "hindi_20": "20",
    "hindi_80": "80",
    "hindi_100": "100",
    "english_20": "20",
    "english_80": "80",
    "english_100": "100",
    "maths_20": "20",
    "maths_80": "80",
    "maths_100": "100",
    "science_20": "20",
    "science_80": "80",
    "science_100": "100",
    "social_science_20": "20",
    "social_science_80": "80",
    "social_science_100": "100",
    "experience_20": "20",
    "experience_80": "80",
    "experience_100": "100",
    "creativity_20": "20",
    "creativity_80": "80",
    "creativity_100": "100",
    "health_20": "20",
    "health_80": "80",
    "health_100": "100",
    "total_marks": "850",
    "parinaam": "PASS",
    "shreni": "shreni",
    "variyata_kramank": "variyata_kramank",
    "examination_center": "inani public school, chittorgarh",
    "examination_date": "29-march-2020",
}

annotatePDF_format3(data)