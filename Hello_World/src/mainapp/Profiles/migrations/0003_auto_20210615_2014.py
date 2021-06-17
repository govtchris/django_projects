# Generated by Django 2.0.7 on 2021-06-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_auto_20210615_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Miss', 'Miss.'), ('', ''), ('Mrs.', 'Mrs.')], default='', max_length=60),
        ),
    ]