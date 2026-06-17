from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Topic
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from .models import Comments

class UserForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Email",
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


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'birthday')

    def save(self, commit=True, join_date=None):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if join_date:
            user.join_date = join_date
        if commit:
            user.save()
        return user
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birthday', 'hobby', 'quote', 'pfp']
        widgets = {
            'birthday': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': "Change Your Birthdate"
            }),
            'hobby': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter/Change Your Hobby"
            }),
            'quote': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter/Change Your Description",
                'rows': 4,
            })
        }
     
        
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']
        widgets =  {
            'topic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Topic',
            }),
           
        }

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data    

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post', 'description', 'image', 'topic']
        widget = {
            'post': forms.TextInput(attrs={
                'class': 'form-controls',
                'placeholder': 'Enter Post Title',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-controls',
                'placeholder': 'Enter Post Description',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-controls',
                'placeholder': 'Put Image Here',
                
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, commit=True, user=None, post_date=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if post_date:
            instance.post_date = post_date
        if commit:
            instance.save()
        return instance

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={
                'class': 'form-controls',
                'placeholder': 'Enter Content',
            }),   
        }