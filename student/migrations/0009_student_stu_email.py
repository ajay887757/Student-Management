# Generated by Django 3.2.4 on 2021-08-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20210810_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_email',
            field=models.EmailField(default='', max_length=30),
        ),
    ]
