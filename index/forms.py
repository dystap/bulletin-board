from django import forms

from index.models import User

class UserForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            "type": "email",
            "class": "form-control",
            "placeholder": "Enter Your Email",
        })
    )

    username = forms.CharField(
        required=True,
        max_length=67,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "placeholder": "Enter Your Username",
        })
    )
    birthday = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
            "placeholder": "Enter Your Birthdate",
        })
    )

    hobby = forms.CharField(
        max_length=67,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Hobby",
        })
    )
    quote = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Description / Quote!",
        })
    )
    pfp = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            "type": "file",
            "placeholder": "Enter Your Profile Picture",
        })

    )

    join_date = forms.DateTimeField(auto_now_add=True)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data    

    def save(self):
        cleaned_data = self.cleaned_data

        User.objects.create(
            email = cleaned_data.get("email"),
            
        )