"""
Definition of models.
"""

from django.db import models

# Create your models here.
from datetime import datetime 
from django.contrib import admin #добавили использование административного модуля
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User # лаба 9

# Модель данных блога
# Модель данных Блога – class Blog


class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name = 'Путь к картинке' ) #лаба 10

# Методы класса:

    def get_absolute_url(self): # метод возвращает строку с URL-адресом записи
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return self.title

# Метаданные – вложенный класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Posts" # имя таблицы для модели
        ordering = ["-posted"] # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога" # тоже для всех статей блога

admin.site.register(Blog)
        # лаба 9 v
class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

# Методы класса:
    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Комментарий {} к {}'.format(self.author, self.post)

# Метаданные – вложенный класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Comments" # имя таблицы для модели
        verbose_name = "Комментарий" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "Комментарий к статьям блога" # тоже для всех статей блога
        ordering = ["-date"] # порядок сортировки данных в модели ("-" означает по убыванию) 
        # лаба 9 ^

admin.site.register(Comment) # лаба 9

class Catalog(models.Model):
    text = models.TextField(verbose_name = "Заказ")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    status = models.TextField(default ="В очереди",verbose_name = "Статус")
# Методы класса:
    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Заказ №{} от {}'.format(self.id,self.author)

        class Meta:
            db_table = "Zakaz" # имя таблицы для модели
            verbose_name = "Заказ" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
            verbose_name_plural = "Заказы пользователей" # тоже для всех статей блога
            ordering = ["-date"] # порядок сортировки данных в модели ("-" означает по убыванию) 

admin.site.register(Catalog)
# лаба 9 ^

#admin.site.register(Catalog) # лаба 9