from django import forms
from Auth.models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','author', 'body', 'category','profile_pic')


        widgets = {
            'title': forms.TextInput(),
            'title_tag': forms.TextInput(),
            'body': forms.Textarea(),
            'category': forms.TextInput(),
            'author': forms.TextInput(attrs={'values':'', 'id' : 'elder', 'type':'hidden'}),
            # 'author': forms.Select(),

        }

