from django import forms

from .models import UserProfile
from .models import Topic
from .models import Post
from .models import Comments

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


    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data    

    def save(self):
        cleaned_data = self.cleaned_data

        User.objects.create(
            email = cleaned_data.get("email"),
            username = cleaned_data.get("username"),
            birthday = cleaned_data.get("birthday"),
            hobby = cleaned_data.get("hobby"),
            quote = cleaned_data.get("quote"),
            pfp = cleaned_data.get("pfp"),
            
        )

class TopicForm(forms.ModelForm):
    class Meta:
        models = Topic
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

    def save(self):
        cleaned_data = self.cleaned_data

        Topic.objects.create(
            topic = cleaned_data.get("topic"),
            
        )

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
                'placeholder': 'Put Image Here'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self):
        cleaned_data = self.cleaned_data
        Post.objects.create(
            post = cleaned_data.get('post'),
            description = cleaned_data.get('description'),
            image = cleaned_data.get('image'),
        )


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