from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
   class Meta:
       model = Article
       fields = ['URL1','URL2',]
       
