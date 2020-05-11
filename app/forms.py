"""
Definition of forms.
"""
from django.db import models 
from .models import Blog 
from .models import Comment 
from .models import Basket 
from .models import News 
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _





class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class CommentForm(forms.ModelForm):           
   class Meta:         
     model = Comment # используемая модель 
     fields = ('text','phone','mail')                 # требуется ввести только поле text         
     labels = {'text': "Комментарий"}    # метка к полю формы text  
# author будет автоматически выбран в зависимости от авторизованного пользователя 
# date автоматически добавляется в момент создания записи 
class BlogForm(forms.ModelForm):      
   class Meta:         
     model = Blog             # используемая модель          
     fields = ('title','description','content','posted',)                 # требуется ввести только поле text         
     labels = {'title': "Заголовок"}    # метка к полю формы title  
# author будет автоматически выбран в зависимости от авторизованного пользователя 
# date автоматически добавляется в момент создания записи 
class NewsForm(forms.ModelForm):      
   class Meta:         
     model = News             # используемая модель          
     fields = ('NewsName','cont','posted',)                 # требуется ввести только поле text         
     labels = {'title': "Заголовок"}    # метка к полю формы title  
class BasketForm(forms.ModelForm):      
   class Meta:         
     model = Basket             # используемая модель          
     fields = ('price','quantity',)                 # требуется ввести только поле text         
           