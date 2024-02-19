from django import forms
from .models import Dart, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DartForm(forms.ModelForm):
    class Meta:
        code = forms.CharField(
            required=True, 
            widget=forms.Textarea(
                attrs={
                    'placeholder': 'Enter your code here',
                    'class': 'form-control'
                }
            )
        )

    class Meta:
        model = Dart
        exclude = ("user", "likes", "dislikes")

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }
        ),
    )
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        ),
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Your password can\'t be too similar to your other personal information.<br>Your password must contain at least 8 characters.<br>Your password can\'t be a commonly used password.<br>Your password can\'t be entirely numeric.</small></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# profile forms
class ProfilePictureForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")

    class Meta:
        model = Profile
        fields = ('profile_image', )