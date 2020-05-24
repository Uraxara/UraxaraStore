"""
Definition of models.
"""


from django.db import models
from django.contrib.auth.models import User  
from datetime import datetime 
from django.contrib import admin
from django.core.urlresolvers import reverse 


# Create your models here.
class Blog(models.Model):     
  title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")     
  description = models.TextField(verbose_name = "Краткое содержание")     
  content = models.TextField(verbose_name = "Полное содержание")     
  posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
  image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке") 

 
  class Meta:                         # метаданные – вложенный класс, который задает дополнительные параметры модели:         
    db_table = "Posts"              # имя таблицы для модели         
    ordering = ["-posted"]          # порядок сортировки данных в модели ("-" означает по убыванию)         
    verbose_name = "статья блога"   # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)         
    verbose_name_plural = "статьи блога"    # тоже для всех статей блога 
admin.site.register(Blog)

# Модель комментариев 
class Comment(models.Model):     
  text = models.TextField(verbose_name = "Комментарий")    
  phone = models.TextField(verbose_name = "Способ связи") 
  mail = models.TextField(verbose_name = "Срок выполнения")  
  date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")     
  author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")        # из модели User (вторичный ключ), каскадное удаление записей в обоих таблицах    
  post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")         # из модели Blog (вторичный ключ),  каскадное удаление записей в обоих таблицах          
  class Meta:                # метаданные - вложенный класс, который задает дополнительные параметры модели:         
    db_table = "Comments"                   # имя таблицы для модели         verbose_name = "Комментарий"         
    verbose_name_plural = "Комментарии статьи блога"
    verbose_name = "Комментарий статьи"
    ordering = ["-date"] 
admin.site.register(Comment)

class Basket(models.Model):
 user = models.ForeignKey(User, on_delete = models.CASCADE)
 item = models.ForeignKey(Blog, on_delete = models.CASCADE)
 price = models.IntegerField(default = 0)
 quantity = models.IntegerField(default = 0)
 class Meta:
  db_table = "Basket"
  verbose_name_plural = "Корзина"
  verbose_name = "Корзина"
admin.site.register(Basket)

class News(models.Model):     
  NewsName = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")         
  cont = models.TextField(verbose_name = "Полное содержание")     
  posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
  imagene = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке") 

 
  class Meta:                         # метаданные – вложенный класс, который задает дополнительные параметры модели:         
    db_table = "news"              # имя таблицы для модели         
    ordering = ["-posted"]          # порядок сортировки данных в модели ("-" означает по убыванию)         
    verbose_name = "статья "   # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)         
    verbose_name_plural = "статьи"    # тоже для всех статей блога 
admin.site.register(News) 
