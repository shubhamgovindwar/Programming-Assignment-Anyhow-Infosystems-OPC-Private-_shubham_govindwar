from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role,related_name='users')



class InventoryRecord(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    ]

    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    batch_num = models.CharField(max_length=20)
    batch_date = models.DateField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    requested_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,blank=True,related_name='approved_inventory' )


