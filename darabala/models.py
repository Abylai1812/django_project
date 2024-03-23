from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Parent(models.Model):
    gender = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    iin = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=128) 
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=gender)

    class Meta:
        verbose_name_plural = "Parents"

class Child(models.Model):
    gender = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=gender)
    documents = models.ImageField(upload_to='docs/imgs', null=True)
    parent = models.ForeignKey('Parent', on_delete=models.CASCADE, related_name='children')

class Daycare(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    director_name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    class Meta:
        verbose_name_plural = "Daycares"

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher_name = models.CharField(max_length=100)
    age_group = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    current_enrollment = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = "Clubs"

class Voucher(models.Model):
    status = [
        ('ACTIVE', 'Active'),
        ('USED', 'Used'),
        ('EXPIRED', 'Expired'),
    ]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=status, default='ACTIVE')
    issued_date = models.DateField()
    child = models.ForeignKey('Child', on_delete=models.SET_NULL, null=True, related_name='vouchers')
    club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True, related_name='vouchers')

    class Meta:
        verbose_name_plural = "Vouchers"

class ChildEnrollment(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    voucher = models.ForeignKey('Voucher', on_delete=models.CASCADE)
    daycare = models.ForeignKey('Daycare', on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey('Club', on_delete=models.CASCADE, blank=True, null=True)
    enrollment_date = models.DateField()

    class Meta:
        verbose_name_plural = "Child Enrollments"
