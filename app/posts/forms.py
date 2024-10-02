from django import forms
from .models import Comment

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea(), max_length=1000)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']