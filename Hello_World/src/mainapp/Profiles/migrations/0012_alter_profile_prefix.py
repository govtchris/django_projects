# Generated by Django 3.2.4 on 2021-06-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0011_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('', ''), ('Dr.', 'Dr.'), ('Miss', 'Miss.')], default='', max_length=60),
        ),
    ]
