# Generated by Django 4.2.1 on 2023-05-16 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_marksheet_report_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolDetail',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=255)),
                ('school_dice_code', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('block', models.CharField(max_length=255)),
                ('kendra_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('scholar_no', models.CharField(max_length=20)),
                ('roll_no', models.CharField(max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schooldetail')),
            ],
        ),
        migrations.CreateModel(
            name='MarksheetFormat2',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('marksheet_id', models.CharField(default='', max_length=20)),
                ('total_grade', models.CharField(max_length=3)),
                ('hindi', models.PositiveSmallIntegerField()),
                ('english', models.PositiveSmallIntegerField()),
                ('science', models.PositiveSmallIntegerField()),
                ('social_science', models.PositiveSmallIntegerField()),
                ('maths', models.PositiveSmallIntegerField()),
                ('sanskrit', models.PositiveSmallIntegerField()),
                ('work_education', models.PositiveSmallIntegerField()),
                ('physical', models.PositiveSmallIntegerField()),
                ('arts', models.PositiveSmallIntegerField()),
                ('examination_year', models.DateField()),
                ('report_card', models.FileField(default=None, max_length=255, null=True, upload_to='pdf_files/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentdetail')),
            ],
        ),
    ]
