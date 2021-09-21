from django import forms  
from .models import Notification 

class notificationForm(forms.ModelForm):  
    class Meta:  
        model = Notification 
        fields = ['author', 'title', 'subtitle', 'desc',  'timestamp']