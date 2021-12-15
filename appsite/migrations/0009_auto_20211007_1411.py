# Generated by Django 3.2.6 on 2021-10-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0008_auto_20211007_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='studentdept',
            field=models.CharField(choices=[('', 'Depertment'), ('Not Applicable', 'Not Applicable'), ('Mechanical', 'Mechanical Engineering'), ('Civil', 'Civil Engineering'), ('Electrical', 'Electrical Engineering'), ('ComputerScience', 'Computer Science Engineering'), ('Electronics&Communication', 'Electronics & Communication Engineering')], default='Computer Science', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.CharField(choices=[('', 'Depertment'), ('Not Applicable', 'Not Applicable'), ('Mechanical', 'Mechanical Engineering'), ('Civil', 'Civil Engineering'), ('Electrical', 'Electrical Engineering'), ('ComputerScience', 'Computer Science Engineering'), ('Electronics&Communication', 'Electronics & Communication Engineering')], default='Computer Science', max_length=40),
        ),
    ]
