# Generated by Django 4.2.1 on 2023-05-17 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_working_education_marksheetformat_1_work_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marksheet',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('marksheet_id', models.CharField(default='', max_length=20)),
                ('total_grade', models.CharField(default='', max_length=3)),
                ('examination_date', models.DateField()),
                ('result', models.CharField(default='', max_length=10)),
                ('shreni', models.CharField(default='', max_length=10)),
                ('percentage', models.CharField(default='', max_length=10)),
                ('report_card', models.FileField(default=None, max_length=255, null=True, upload_to='pdf_files/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMark',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('hindi', models.CharField(default='', max_length=5)),
                ('english', models.CharField(default='', max_length=5)),
                ('maths', models.CharField(default='', max_length=5)),
                ('sanskrit', models.CharField(default='', max_length=5)),
                ('environmental_studies', models.CharField(default='', max_length=5)),
                ('work_education', models.CharField(default='', max_length=5)),
                ('physical', models.CharField(default='', max_length=5)),
                ('arts', models.CharField(default='', max_length=5)),
                ('science', models.CharField(default='', max_length=5)),
                ('social_science', models.CharField(default='', max_length=5)),
                ('hindi_20', models.CharField(default='', max_length=3)),
                ('hindi_80', models.CharField(default='', max_length=3)),
                ('hindi_100', models.CharField(default='', max_length=3)),
                ('english_20', models.CharField(default='', max_length=3)),
                ('english_80', models.CharField(default='', max_length=3)),
                ('english_100', models.CharField(default='', max_length=3)),
                ('maths_20', models.CharField(default='', max_length=3)),
                ('maths_80', models.CharField(default='', max_length=3)),
                ('maths_100', models.CharField(default='', max_length=3)),
                ('science_20', models.CharField(default='', max_length=3)),
                ('science_80', models.CharField(default='', max_length=3)),
                ('science_100', models.CharField(default='', max_length=3)),
                ('sanskrit_20', models.CharField(default='', max_length=3)),
                ('sanskrit_80', models.CharField(default='', max_length=3)),
                ('sanskrit_100', models.CharField(default='', max_length=3)),
                ('social_science_20', models.CharField(default='', max_length=3)),
                ('social_science_80', models.CharField(default='', max_length=3)),
                ('social_science_100', models.CharField(default='', max_length=3)),
                ('work_education_20', models.CharField(default='', max_length=3)),
                ('work_education_80', models.CharField(default='', max_length=3)),
                ('work_education_100', models.CharField(default='', max_length=3)),
                ('arts_20', models.CharField(default='', max_length=3)),
                ('arts_80', models.CharField(default='', max_length=3)),
                ('arts_100', models.CharField(default='', max_length=3)),
                ('physical_20', models.CharField(default='', max_length=3)),
                ('physical_80', models.CharField(default='', max_length=3)),
                ('physical_100', models.CharField(default='', max_length=3)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentdetail')),
            ],
        ),
        migrations.RemoveField(
            model_name='marksheetformat_2',
            name='student',
        ),
        migrations.RemoveField(
            model_name='marksheetformat_3',
            name='student',
        ),
        migrations.DeleteModel(
            name='MarksheetFormat_1',
        ),
        migrations.DeleteModel(
            name='MarksheetFormat_2',
        ),
        migrations.DeleteModel(
            name='MarksheetFormat_3',
        ),
        migrations.AddField(
            model_name='marksheet',
            name='marks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentmark'),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentdetail'),
        ),
    ]