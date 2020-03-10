from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    weight = models.FloatField()
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Instructor(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    weight = models.FloatField()

    def __str__(self):
        return f'{self.name} {self.surname}'

class Lesson(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    student = models.ManyToManyField(Student, through='Lesson_to_Person')
    instructor = models.ManyToManyField(Instructor, through='Lesson_to_Person')
    duration = models.FloatField()
    paid = models.BooleanField(default=False)

class Lesson_to_Person(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING, null=True, blank=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True, blank=True)


