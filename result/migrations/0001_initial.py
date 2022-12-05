# Generated by Django 4.0.6 on 2022-12-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tcr', models.IntegerField()),
                ('tce', models.IntegerField()),
                ('gpa', models.FloatField()),
                ('cgpa', models.FloatField()),
            ],
        ),
    ]
