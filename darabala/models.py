from django.db import models

class Parents(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    iin = models.CharField(max_length=12)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Parents"

class Children(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    documents = models.ImageField(upload_to='docs/imgs', null=True)
    parent = models.ForeignKey('Parents', on_delete=models.CASCADE)

class Daycares(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    director_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    class Meta:
        verbose_name_plural = "Daycares"
    
class Clubs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    teacher_name = models.CharField(max_length=100)
    age_group = models.CharField(max_length=50)
    capacity = models.IntegerField()
    current_enrollment = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name_plural = "Clubs"
    
class Vouchers(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    status = models.CharField(max_length=20)
    issued_date = models.DateField()
    child = models.ForeignKey('Children', on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = "Vouchers"
    
class ChildEnrollment(models.Model):
    child = models.ForeignKey('Children', on_delete=models.CASCADE)
    voucher = models.ForeignKey('Vouchers', on_delete=models.CASCADE)
    daycare = models.ForeignKey('Daycares', on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey('Clubs', on_delete=models.CASCADE, blank=True, null=True)
    enrollment_date = models.DateField()