# Generated by Django 2.0.7 on 2021-06-15 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0007_auto_20210615_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Miss', 'Miss.'), ('', ''), ('Mrs.', 'Mrs.')], default='--', max_length=60),
        ),
    ]
