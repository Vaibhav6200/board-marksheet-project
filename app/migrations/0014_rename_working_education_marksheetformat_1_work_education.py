# Generated by Django 4.2.1 on 2023-05-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_kendra_code_schooldetail_examination_center_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marksheetformat_1',
            old_name='working_education',
            new_name='work_education',
        ),
    ]