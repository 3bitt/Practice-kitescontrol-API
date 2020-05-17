from django.db import models


class Instructor(models.Model):
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
    nickname = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=False, blank=False)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.CharField(max_length=40, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)
    iko_level = models.CharField(max_length=4, choices=IKO_LEVELS, default='None')
    pay_rate = models.IntegerField(null=True, blank=True)
    english_lessons = models.BooleanField(null=True, blank=True)
    kids_lessons = models.BooleanField(null=True, blank=True)
    group_lessons = models.BooleanField(null=True, blank=True)
    daily_hour_limit = models.FloatField(null=True, blank=True)
    active = models.BooleanField(blank=True, default=True)


    def __str__(self):
        return f'{self.name} {self.surname}'
