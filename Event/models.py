from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


EVENT_CATEGORY_CHOICES = (
    ('Conference','Conference'),
    ('Seminar', 'Seminar'),
    ('Presentation','Presentation'),
)

class Event(models.Model):
    #author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    Event_id = models.CharField(max_length=30,default='')
    Event_name = models.CharField(max_length=30,default='')
    Event_description = models.TextField(blank=True)
    Event_category = models.CharField(max_length=30, choices=EVENT_CATEGORY_CHOICES, default='Conference')
    Event_start_date = models.DateField(default='2019-12-12')
    Event_end_date = models.DateField(default='2019-12-12')
    Event_start_time = models.TimeField(default='06:00:00')
    Event_end_time = models.TimeField(default='08:00:00')
    Event_location = models.CharField(max_length=30,default='')
    Allow_registration = models.BooleanField(default=True)
    Event_image = models.ImageField(upload_to='event/%Y/%m/%d', blank=True, default ="/media/event/2019/12/20/event4.jpg")
    Adult_ticket_price = models.DecimalField(max_digits=10, decimal_places=2,default = 0)
    Child_ticket_price = models.DecimalField(max_digits=10, decimal_places=2,default = 0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Event_id

    def get_absolute_url(self):
        return reverse('event_details',kwargs={'pk':self.pk})

class Registration(models.Model):
    #author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    Registration_id = models.CharField(max_length=30,default='')
    Event_name = models.CharField(max_length=30,default='')
    First_name = models.CharField(max_length=30,default='')
    Last_name = models.CharField(max_length=30,default='')
    Email_id = models.CharField(max_length=30,default='')
    Contact = models.CharField(max_length=30,default='')
    Address = models.CharField(max_length=30,default='')
    Total_adult_qty = models.IntegerField(validators=[MinValueValidator(0)])
                                       #MaxValueValidator(50)])
    Total_child_qty = models.IntegerField(validators=[MinValueValidator(0)])
                                       #MaxValueValidator(50)])
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Registration_id

    def get_absolute_url(self):
        return reverse('registration_details',kwargs={'pk':self.pk})