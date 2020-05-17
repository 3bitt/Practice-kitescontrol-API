from django.db import models

class Student(models.Model):
    IKO_LEVELS = (
        ('None', 'None'),
        ('AITC', 'Assistant'),
        ('1', 'Level 1'),
        ('2', 'Level 2'),
        ('3', 'Level 3'),
        ('HI', 'Head Instructor')
    )

    name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    weight = models.FloatField()
    arrival_date = models.DateField(null=True, blank=True)
    leave_date = models.DateField(null=True, blank=True)
    email_address = models.CharField(max_length=40, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    stay_location = models.CharField(max_length=40, null=True, blank=True)
    iko_level = models.CharField(max_length=4, choices=IKO_LEVELS, default='None')
    comment = models.CharField(max_length=255, null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    # https://stackoverflow.com/questions/34275588/djangorestframework-modelserializer-datetimefield-only-converting-to-current-tim
    def __str__(self):
        return f'{self.name} {self.surname}'

