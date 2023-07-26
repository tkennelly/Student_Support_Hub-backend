from django.db import models

class User(models.Model):
    USER_TYPE = (
    ('T', 'Teacher'),
    ('C', 'Caseworker'),
)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    clearance = models.CharField(max_length=1, choices=USER_TYPE)

    def __str__(self):
        return self.username
    
class Accomodation(models.Model):
    student_name = models.CharField(max_length=20, default='name')
    bullet_list = models.TextField()

    def __str__(self):
        return self.student_name
    
class Student(models.Model):
    LEARNING_TYPE = (
    ('IEP', 'Individualized Educational Plan'),
    ('504', '504 Plan'),
)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    learning_plan = models.CharField(max_length=3, choices=LEARNING_TYPE)
    teachers = models.ManyToManyField(User, related_name='teachers')
    caseworker = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='caseworker', blank=True, null=True)
    accomodations = models.ForeignKey(Accomodation, on_delete=models.DO_NOTHING, related_name='accomodations', blank=True, null=True)
    teacher_suggestions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.first_name
