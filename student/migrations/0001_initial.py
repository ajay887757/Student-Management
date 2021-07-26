# Generated by Django 3.2.4 on 2021-07-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stu_id', models.CharField(max_length=100, unique=True)),
                ('stu_fname', models.CharField(default='', max_length=100)),
                ('stu_lname', models.CharField(default='', max_length=100)),
                ('stu_branch', models.CharField(default='', max_length=100)),
                ('stu_age', models.IntegerField(default='15')),
                ('stu_contact', models.IntegerField(default='')),
            ],
        ),
    ]
