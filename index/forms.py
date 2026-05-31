from django import forms
from django.contrib.auth.models import User
from .models import Topic
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from .models import Comments

class UserForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailField(attrs={
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
    # hobby = forms.CharField(
    #     max_length=67,
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Hobby",
    #     })
    # )
    # quote = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(attrs={
    #         "class": "form-control",
    #         "placeholder": "Enter Your Description / Quote!",
    #     })
    # )
    # pfp = forms.FileField(
    #     required=False,
    #     widget=forms.FileInput(attrs={
    #         "type": "file",
    #         "placeholder": "Enter Your Profile Picture",
    #     })

    # )

    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'birthday')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            from .models import Profile
            Profile.objects.create(
                user=user, 
                birthday=self.cleaned_data['birthday']
            )
            
        return user
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
    
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

class CommentForm(forms.ModelForm):
    class Meta: 
        models = Comments
        fields = ['post', 'comment']
        widget = {
            'post': forms.TextInput(attrs={
                'class': 'form-controls',
                'placeholder': 'Enter Comment Title',
            }),
            'comment': forms.TextInput(attrs={
                'class': 'form-controls',
                'placeholder': 'Enter Comment Content',
            }),   
        }