from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from .models import Myuser
from .form import UserForm


#@login_required
def user_list(request):
    users = Myuser.objects.all()
    adminusers = Myuser.objects.filter(role='admin')
    allusers = Myuser.objects.all()
    return render(request, 'User/user_list.html', {'users':users,'adminusers':adminusers,'allusers':allusers})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = form.save()
            #login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            users = Myuser.objects.all()
            User.objects.create_user(username=username, password=raw_password, email=email)
            return render(request, 'User/user_list.html', {'users':users})
    else:
        form = UserForm()
        return render(request, 'User/user_edit.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(Myuser, pk=pk)
    user.delete()
    messages.success(request, "User successfully deleted!")
    return HttpResponseRedirect("/user/")


    #return render(request,'User/user_list.html', {'user':user})

def user_edit(request, pk):
    user = get_object_or_404(Myuser, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=True)
            username = form.cleaned_data.get('username')
            newpassword = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            try:
                User.objects.get(username=username)
            except:
                User.objects.filter(username=username).delete()
                User.objects.create_user(username=username, password=newpassword, email=email)
            else:
                user1 = User.objects.get(username=username)
                user1.set_password(newpassword)
                user1.save()
            return HttpResponseRedirect("/user/")
    else:
        form = UserForm(instance=user)
        return render(request, 'User/user_edit.html', {'form': form})


def signup(request):
    #if request.method == 'POST':
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        username = form.cleaned_data.get('username')
    #        raw_password = form.cleaned_data.get('password1')
    #        user = authenticate(username=username, password=raw_password)
    #        login(request, user)
    #        return HttpResponseRedirect("/user/")
    #else:
    #    form = UserCreationForm()
    #return render(request, 'User/signup.html', {'form': form})
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = form.save()
            #login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            users = Myuser.objects.all()
            User.objects.create_user(username=username, password=raw_password, email=email)
            return render(request, 'User/user_list.html', {'users':users})
    else:
        form = UserForm()
        return render(request, 'User/user_edit2.html', {'form': form})

