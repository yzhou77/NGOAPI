from django.contrib.auth.forms import UserCreationForm

from .models import Myuser
from django import forms



class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=(("user",("user")),("admin",("admin"))))
    class Meta:
        model = Myuser
        fields = ('firstName','lastName','email', 'username', 'password', 'role')

#class SignUpForm(UserCreationForm):

 #   firstName = forms.CharField(max_length=30, required=False, help_text='Optional.')
  #  lastName = forms.CharField(max_length=30, required=False, help_text='Optional.')
   # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #role = forms.ChoiceField(choices=(("user",("user")),("admin",("admin"))))
    #class Meta:
     #   model = Myuser
      #  fields = ('firstName','lastName','email','username',  'password', 'role')