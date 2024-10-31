from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,"id":"message-name" , 'placeholder':"Your name" ,'aria-label':"Ім'я"
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type':"password" , 'class':'ml-a', 'placeholder':"Your password" ,'aria-label':"Пароль"
    }))
    

    class Meta:
        model = User
        fields = ('username','password',)

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,'class':'','placeholder':"Ім'я"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,'class':'ml-a','placeholder':'Прізвище'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,'class':'','placeholder':'Нікнейм'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'type':"email" ,'class':'ml-a','placeholder':'Електронна пошта'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'type':"password" ,'class':'','placeholder':'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'type':"password" ,'class':'ml-a','placeholder':'Ще раз пароль'
    }))
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2',)

class UserCangeDataForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','image', 'username', 'email',)

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':''
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':''
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': '', 'placeholder': ''
    }), required=False)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'', 'readonly':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control','placeholder':'', 'readonly':True
    }))

