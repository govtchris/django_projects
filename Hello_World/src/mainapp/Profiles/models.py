from django.db import models

PREFIXES = {
    ('', ''),
    ('Mr.', 'Mr.'),
    ('Miss', 'Miss.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
}


class Profile(models.Model):
    Prefix = models.CharField(max_length=60, default='', blank=True, null=False, choices=PREFIXES)
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.EmailField(max_length=60, default="", blank=True, null=False)
    Username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name

