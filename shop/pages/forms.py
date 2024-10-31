
from django import forms
from .models import Comments

class CommentCreateForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'aria-label':"Input for writing message",'rows':"5",'class':'','placeholder':'Тут можна писати'
    }))



