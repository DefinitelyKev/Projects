from django import forms
from .models import Review
from django.forms import ModelForm

# class Reviewform(forms.Form):
# first_name = forms.CharField(label="First Name", max_length=100)
# last_name = forms.CharField(label="Last Name", max_length=100)
# email = forms.EmailField(label="Email")
# review = forms.CharField(
# label="Please write your review here",
# widget=forms.Textarea(attrs={"class": "myform", "rows": "4", "cols": "50"}),
# )
#


class Reviewform(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "first_name": "Your First Name",
            "last_name": "Last Name",
            "stars": "Rating",
        }
        error_messages = {
            "stars": {
                "min_value": "Dawg too low",
                "max_value": "Dawg too high",
            }
        }
