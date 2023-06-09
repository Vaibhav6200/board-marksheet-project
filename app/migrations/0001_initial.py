# Generated by Django 4.0 on 2023-04-15 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('scholar_no', models.CharField(max_length=20)),
                ('roll_no', models.CharField(max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('student_class', models.PositiveSmallIntegerField()),
                ('school_name', models.CharField(max_length=255)),
                ('block', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('school_dice_code', models.CharField(max_length=255)),
                ('examination_center', models.CharField(max_length=255)),
                ('examination_center_code', models.CharField(max_length=50)),
                ('markSheetCode', models.AutoField(editable=False, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1000000)])),
                ('grade', models.CharField(max_length=3)),
                ('average', models.PositiveSmallIntegerField()),
                ('examination_date', models.DateField()),
                ('subject1', models.PositiveSmallIntegerField()),
                ('subject2', models.PositiveSmallIntegerField()),
                ('subject3', models.PositiveSmallIntegerField()),
                ('subject4', models.PositiveSmallIntegerField()),
                ('subject5', models.PositiveSmallIntegerField()),
                ('subject6', models.PositiveSmallIntegerField()),
                ('subject7', models.PositiveSmallIntegerField()),
                ('subject8', models.PositiveSmallIntegerField()),
                ('subject9', models.PositiveSmallIntegerField()),
                ('report_card', models.FileField(upload_to='pdf_files/')),
            ],
        ),
    ]
