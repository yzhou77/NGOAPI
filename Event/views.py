from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from Event.models import Event
from User.models import Myuser
from Event.models import Registration
from django.utils import timezone
from .forms import EventForm
from .forms import EventForm1
from .forms import PForm
from .forms import RForm
from .forms import RegistrationForm
from .cart import Cart

def event_list(request):
    events = Event.objects.filter(published_date__lte=timezone.now())
    adminusers = Myuser.objects.filter(role='admin')
    allusers = Myuser.objects.all()
    return render(request, 'eventlist.html', {'events':events,'adminusers':adminusers})

def event_details(request,pk):
	event = get_object_or_404(Event,pk=pk)
	return render(request,'eventdetails.html',{'event':event})

def event_new(request):
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			event = form.save(commit=False)
			event.author = request.user
			event.published_date=timezone.now()
			event.save()
			return redirect('event_details',pk=event.pk)
	else:
		form = EventForm()
		return render(request,'eventedit.html',{'form':form})

def update(request,pk):
	return render(request,'update.html')

class EventCreate(CreateView):
    model = Event
    template_name = 'eventform.html'
    form_class = PForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)

def user_view(request):
	events = Event.objects.filter(published_date__lte=timezone.now())
	adminusers = Myuser.objects.filter(role='admin')
	allusers = Myuser.objects.all()
	return render(request, 'userview.html', {'events': events, 'adminusers':adminusers,'allusers':allusers})

def registration(request):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'registration.html', {'event': event})

class EventRegistration(CreateView):
    model = Registration
    template_name = 'registrationform.html'
    form_class = RForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventRegistration, self).form_valid(form)

def registration_details(request,pk):
	registration = get_object_or_404(Registration,pk=pk)
	return render(request,'registrationdetails.html',{'registration':registration})

def event_registration(request,pk):
	event = get_object_or_404(Event, pk=pk)
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			registration = form.save(commit=False)
			registration.author = request.user
			registration.Event_name = event.Event_name
			registration.published_date=timezone.now()
			registration.save()
			# return redirect('registration_details',pk=registration.pk)
		return redirect('registration_confirmation', pk=registration.pk,pl=pk)
	else:
		form = RegistrationForm()
		return render(request,'registrationedit.html',{'form':form,'event':event})

def registration_confirmation(request,pk,pl):
	registration = get_object_or_404(Registration,pk=pk)
	event = get_object_or_404(Event, pk=pl)
	return render(request,'registrationconfirmation.html',{'registration':registration,'event':event})

def confirmed(request,pk):
	event = get_object_or_404(Event, pk=pk)
	return render(request, 'confirmed.html', {'event': event})