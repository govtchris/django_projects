# Generated by Django 3.2.4 on 2021-06-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0016_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Dr.', 'Dr.'), ('', ''), ('Mrs.', 'Mrs.'), ('Miss', 'Miss.')], default='', max_length=60),
        ),
    ]
