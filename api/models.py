from django.db import models

# Create your models here.

IKO_LEVELS = (
    ('None', 'None'),
    ('AITC', 'Assistant'),
    ('1', 'Level 1'),
    ('2', 'Level 2'),
    ('3', 'Level 3'),
    ('HI', 'Head Instructor')
)


class Student(models.Model):
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

    def __str__(self):
        return f'{self.name} {self.surname}'

class Instructor(models.Model):
    # IKO_LEVELS = (
    #     ('None', 'None'),
    #     ('AITC', 'Assistant'),
    #     ('1', 'Level 1'),
    #     ('2', 'Level 2'),
    #     ('3', 'Level 3'),
    #     ('HI', 'Head Instructor')
    # )

    name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, null=False, blank=False)
    nickname = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=False, blank=False)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
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

class Lesson(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    student = models.ManyToManyField(Student, related_name='lessons')
    instructor = models.ManyToManyField(Instructor, related_name='lessons')
    duration = models.FloatField()
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=30, null=True, blank=True)
    equipment = models.CharField(max_length=30, null=True, blank=True)
    kite_brand = models.CharField(max_length=30, null=True, blank=True)
    kite_size = models.FloatField(null=True, blank=True)
    board = models.CharField(max_length=30, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)


class Schedule(models.Model):
    date = models.DateField(null=False, blank=False)
    lessons = models.ManyToManyField(Lesson, related_name='lesson')
    finalized = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f'Schedule {self.pk} - {self.date}'
