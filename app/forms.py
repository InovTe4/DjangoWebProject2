"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models # Лаба 9
from .models import Comment  # Лаба 9
from .models import Blog #лаба 10
from .models import Catalog #New

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class Support(forms.Form):
        name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
        city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
        gender = forms.ChoiceField(label='Ваш пол',
                                  choices=[('1','Мужской'),('2','Женский')],
                                  widget=forms.RadioSelect, initial=1)
        face = forms.ChoiceField(label='Вы являетесь', 
                                     choices=(('1','индивидуальным предпринимателем'),
                                     ('2','физическим лицом'),
                                     ('3','юридическим лицом'),
                                     ('4','организацией')), initial=1)
        email = forms.EmailField(label='Ваш e-mail', min_length=7)
        message = forms.CharField(label='Текст обращения', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm (forms.ModelForm): # Лаба 9 v
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text 
        #author будет автоматически выбран в зависимости от авторизованного пользователя
        # date автоматически добавляется в момент создания записи
        
        # лаба 10 v

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content','image',)
        labels = {'title':"Заголовок",'description':"Краткое содержание",'content':"Полное содержание",'image':"Изображение"}
        # лаба 10 ^

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "",} # метка к полю формы text
