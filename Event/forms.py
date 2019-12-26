from datetime import datetime
from django.db import models

from .models import Event
from .models import Registration
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

# If creating form using ModelForm
class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('Event_id','Event_name','Event_description','Event_category','Event_start_date','Event_end_date',\
                  'Event_start_time','Event_end_time','Event_location','Allow_registration','Event_image','Adult_ticket_price',\
                  'Child_ticket_price')

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
		fields = ('First_name','Last_name','Email_id','Contact','Address','Total_adult_qty','Total_child_qty')

EVENT_CATEGORY_CHOICES = (
    ('Conference','Conference'),
    ('Seminar', 'Seminar'),
    ('Presentation','Presentation'),
)

class EventForm1(forms.Form):
    Event_id = models.CharField(max_length=30, default='')
    Event_name = models.CharField(max_length=30, default='')
    Event_description = models.TextField(blank=True)
    Event_category = models.CharField(max_length=30, choices=EVENT_CATEGORY_CHOICES, default='Conference')
    Event_start_date = models.DateField()
    Event_end_date = models.DateField()
    Event_start_time = models.TimeField()
    Event_end_time = models.TimeField()
    Event_location = models.CharField(max_length=30, default='')
    Allow_registration = models.BooleanField(default=True)
    Event_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    Adult_ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    Child_ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

from django.forms import ModelForm

class PForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('user', 'date',)

class RForm(ModelForm):
    class Meta:
        model = Registration
        exclude = ('user', 'date',)