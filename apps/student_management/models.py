from django.db import models
import uuid

# Create your models here.
class Student(models.Model):

    GENDER_CHOICES = (
        ['m', 'Male'],
        ['f', 'Female']
    )

    CURRENT_LEVEL_CHOICES = [
        ('G1', 'Grade 1'),
        ('G2', 'Grade 2'),
        ('G3', 'Grade 3'),
        ('G4', 'Grade 4'),
        ('G5', 'Grade 5'),
        ('G6', 'Grade 6'),
        ('G7', 'Grade 7'),
        ('G8', 'Grade 8'),
        ('G9', 'Grade 9'),
        ('G10', 'Grade 10'),
        ('G11', 'Grade 11'),
        ('G12', 'Grade 12'),
    ]
    
    ENROLLMENT_STATUS_CHOICES =(
        ['active', 'Active'],
        ['dismissed', 'Dismissed'],
        ['graduated', 'Graduated'],
        ['transferred', 'Transferred'],
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name',max_length=50)
    birth_date = models.DateField('Birth Date')
    gender = models.CharField('Gender', max_length=10, choices=GENDER_CHOICES, default='m')
    current_academic_level = models.CharField('current_academic_level', max_length=30, choices=CURRENT_LEVEL_CHOICES)
    enrollment_status = models.CharField('Enrollment Status', max_length=20, choices=ENROLLMENT_STATUS_CHOICES)
    photo = models.ImageField('Photo', upload_to='students/photos', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    
    def get_age(self):
        from datetime import date
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) <(self.birth_date.month, self.birth_date.day))
        return age 
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'date') # Prevents marking a student twice on the same day