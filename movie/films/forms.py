from django.forms import ModelForm
from django import forms
from .models import Comment, Rating, RatingStar


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.Textarea}


class RatingForm(ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ("star", )