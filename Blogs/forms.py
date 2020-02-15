from django import forms
from .models import Topic, Blog

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):      
    class Meta:          
        model = Blog         
        fields = ['text']         
        labels = {'text': ''}        
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}