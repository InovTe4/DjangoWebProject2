"""
Definition of views.
"""

from django.shortcuts import render, redirect
from app.forms import BlogForm # лаба 6
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import Support
from django.contrib.auth.forms import UserCreationForm # лаба 6
from django.db import models # лаба 8 
from .models import Blog # лаба 8
from .models import Comment # использование модели комментариев, лаба 9
from .forms import CommentForm # использование формы ввода комментария, лаба 9
from .models import Catalog # использование модели комментариев
from .forms import CatalogForm # использование формы ввода комментария

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О Нас',
            'message':'Сведения о нашей компании',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Сведения о средах разработки',
            'year':datetime.now().year,
        }
    )

def developers(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/developers.html',
        {
            'title':'Наши разработчики',
            'message':'Клнтакты наших разработчиков',
            'year':datetime.now().year,
        }
    )

def pool(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина','2':'Женщина'}
    face = {'1': 'индивидуальным предпринимателем',
                '2': 'физическим лицом',
                '3': 'юридическим лицом',
                '4': 'организацией'}
    if request.method == 'POST':
        form = Support(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['gender'] =gender[ form.cleaned_data['gender']]
            data['face'] = face [form.cleaned_data['face']]
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = Support()
    return render(
        request,
        'app/pool.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request): # лаба 6 v
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('login') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
    return render(
        request,
        'app/registration.html',
        {

        'regform': regform, # передача формы в шаблон веб-страницы
        'year':datetime.now().year,
        }
    ) # лаба 6 ^

def blog(request): # лаба 8 v
    """Renders the blog page."""
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Полезные статьи',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year':datetime.now().year,
        }

    ) # лаба 8 ^

def blogpost(request, parametr): # лаба 8 v
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr) # запрос на выбор всех комментариев статьи лаба 9 v
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария лаба 9 ^

    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы лаба 9
            'form': form, # передача формы добавления комментария в шаблон веб-страницы лаба 9
            'year':datetime.now().year,
        }
    ) # лаба 8 ^

def newpost(request): # лаба 10 v
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':                # после отправки формы
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()                       #сохраняем изменения после добавления полей
            return redirect('blog')             # переадресация на страницуц Блог после создания статьи Блога
    else:
        blogform = BlogForm()                  # создание объекта формы ввода данных


    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,               # передача формы в шаблон веб-страницы
            'title': 'Добавить статью блога',
            'year':datetime.now(),
            }
        )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'О Нас',
            'message':'Сведения о нашей компании',
            'year':datetime.now().year,
        }
    )
# лаба 10 ^

def catalog(request): #New1
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    zakaz = Catalog.objects.filter # запрос на выбор всех комментариев статьи лаба 9 v

    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CatalogForm(request.POST)
        if form.is_valid():
            zakaz_f = form.save(commit=False)
            zakaz_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            zakaz_f.save() # сохраняем изменения после добавления полей
            return redirect('basket') # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CatalogForm() # создание формы для ввода комментария лаба 9 ^
    return render(
        request,
        'app/catalog.html',
        {
            'zakaz': zakaz, # передача всех комментариев к данной статье в шаблон веб-страницы лаба 9
            'form': form, # передача формы добавления комментария в шаблон веб-страницы лаба 9
        }
    ) 

def basket(request): #New1 
    """Renders the links page."""
    assert isinstance(request,HttpRequest)
    zakaz = Catalog.objects.filter(author = request.user) # запрос на выбор заказа текущего пользователя
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        if form.is_valid():
            zakaz_f = form.save(commit=False)
            zakaz_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            zakaz_f.save() # сохраняем изменения после добавления полей
            return redirect('basket') # переадресация на ту же страницу статьи после отправки комментария
    return render(
        request,
        'app/basket.html',
        {
            'zakaz': zakaz, # передача всех комментариев к данной статье в шаблон веб-страницы лаба 9         
        }
    ) # лаба 8 ^


def delete(request,parametr1): #New1
    zakaz_f = Catalog.objects.get(id=parametr1) # запрос на выбор всех комментариев статьи лаба 9 v
    zakaz_f.delete()
    zakaz = Catalog.objects.filter(author = request.user)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CatalogForm(request.POST)
    return render(
        request,
        'app/basket.html',
        {
            'zakaz': zakaz, # передача всех комментариев к данной статье в шаблон веб-страницы лаба 9
        }
    ) 

def calculator(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/calculator.html',
        {
            'title':'О Нас',
            'message':'Сведения о нашей компании',
            'year':datetime.now().year,
        }
    )

def summ (url):
    return "window.location=" + url +"";

