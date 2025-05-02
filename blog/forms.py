from django import forms
from .models import Comment, Post


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        model: Post
        fields = ('name', 'email', 'to', 'body')


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    body = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    class Meta:
        model= Comment
        fields = ('name', 'email', 'body')