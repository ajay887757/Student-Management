# Generated by Django 3.2.4 on 2021-08-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210810_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_email',
            field=models.EmailField(default='', max_length=30),
        ),
    ]
