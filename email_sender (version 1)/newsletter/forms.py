from .models import EmailSubmit
from django.forms import ModelForm


class EmailForm(ModelForm):
    class Meta:
        model = EmailSubmit
        fields = "__all__"

        # labels = {
        #     "email_user": "Email",
        #     "title": "Subject",
        #     "description": "Message",
        # }
