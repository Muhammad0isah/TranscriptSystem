# Generated by Django 4.0.6 on 2022-12-04 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_student_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_image',
        ),
    ]
