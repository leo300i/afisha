from django import forms
from main_app.models import Movie
from django.contrib.auth.models import User


class CreateMoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title descriptions director'.split()

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название!',
                    'rows': 10
                }
            ),
            'descriptions': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                }
            ),
            'director': forms.Select(
                attrs={
                    'class': 'form-control form-control-custom',

                }
            )
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter a password'
        }
    ))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter a password'
        }
    ))
    password_key = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'repeat a password'
        }
    ))

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password)
        return user