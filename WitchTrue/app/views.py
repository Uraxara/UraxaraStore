"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import Comment    # использование модели комментариев 
from .forms import CommentForm         # использование формы ввода комментария 
from django.db import models 
from .models import Blog 
from .forms import BlogForm
from .models import Basket 
from .forms import BasketForm
from .models import News
from .forms import NewsForm


from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    posts = Comment.objects.all()
    return render(
    request,
    'app/index.html',
    { 'posts': posts,
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
            'title':'Проекты',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def call(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/call.html',
        {
            'title':'Контакты',
            'message':'Контактная информаия',
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
            'title':'О магазине',
            'message':'Подзаголовок',
            'year':datetime.now().year,
        }
    )
    
def links(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Каталог',
            'year':datetime.now().year,
        }
    )
def a1(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/a1.html',
        {
            'title':'Игровые приставки',
            'year':datetime.now().year,
        }
    )
def a2(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/a2.html',
        {
            'title':'Аксессуары к консолям',
            'year':datetime.now().year,
        }
    )
def a3(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/a3.html',
        {
            'title':'Игровые консоли с аксессуарами',
            'year':datetime.now().year,
        }
    )    
def registration(request):
    """Renders the registration page."""
    if request.method == "POST":            # после отправки формы
       regform = UserCreationForm(request.POST)          
       if regform.is_valid():                #валидация полей формы
           reg_f = regform.save(commit=False)   # не сохраняем данные формы
           reg_f.is_staff = False  # запрещен вход в административный раздел
           reg_f.is_active = True                       # активный пользователь        
           reg_f.is_superuser = False            # не является суперпользователем           
           reg_f.date_joined = datetime.now()           # дата регистрации
           reg_f.last_login = datetime.now()               # дата последней авторизации\
       
           reg_f.save()                                 # сохраняем изменения после добавления данных (добавление пользователя в БД пользователей)
        
           return redirect('home')                     # переадресация на главную страницу после регистрации
    else:                                                    
      regform = UserCreationForm()                     # создание объекта формы для ввода данных нового пользователя         
    assert isinstance(request, HttpRequest)
    return render(         
     request,
     'app/registration.html',         
     { 
         
       'regform': regform,           # передача формы в шаблон веб-страницы  
            
       'year':datetime.now().year,         
     }     
    )
def blog(request):
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели 
    return render(         
     request,         
     'app/blog.html',         
     {                     # параметр в {} – данные для использования в шаблоне.             
       'title':'Блог',             
       'posts': posts,                         # передача списка статей в шаблон веб-страницы              
       'year':datetime.now().year,         
     }     
   ) 
def blogpost(request, parametr):     
  """Renders the blogpost page."""     
  post_1 = Blog.objects.get(id=parametr)      # запрос на выбор конкретной статьи по параметру 
  comments = Comment.objects.filter(post=parametr)
  if request.method == "POST":                            # после отправки данных формы на сервер методом POST         
      form = CommentForm(request.POST)         
      if form.is_valid():             
          comment_f = form.save(commit=False)             
          comment_f.author = request.user                       # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя             
          comment_f.date = datetime.now()                       # добавляем в модель Комментария (Comment) текущую дату                                    
          comment_f.post = Blog.objects.get(id=parametr)        # добавляем в модель Комментария (Comment) статью, для которой данный комментарий                 
          comment_f.save()                                      # сохраняем изменения после добавления полей   
          return redirect('blogpost', parametr=post_1.id)     # переадресация на ту же страницу статьи после отправки комментария     
  else:                                                    
     form = CommentForm()                                 # создание формы для ввода комментария 
  assert isinstance(request, HttpRequest)     
  return render(         
    request,         
    'app/blogpost.html',         
    {                                                        
      'post_1': post_1,                  # передача конкретной статьи в шаблон веб-страницы                
      'comments': comments,              # передача всех комментариев к данной статье в шаблон веб-страницы              
      'form': form,                      # передача формы в шаблон вебстраницы
   
       'year':datetime.now().year, 
    } 
  )
def get_absolute_url(self):         # метод возвращает строку с уникальным интернет-адресом записи 
    return reverse("blogpost", args = [str(self.id)]) 
    
def __str__(self):                  # метод возвращает название, используемое для представления отдельных записей в административном разделе         
    return self.title 
def post(request):
    posts = Blog.objects.all()
    if request.method == "POST":                            # после отправки данных формы на сервер методом POST         
      form = BlogForm(request.POST)         
      if form.is_valid(): 	  
            form.save()                             # сохраняем изменения после добавления полей   
            return redirect('post')     # переадресация на ту же страницу статьи после отправки комментария     
    else:                                                    
     form = BlogForm()                                 # создание формы для ввода комментария 
  
    assert isinstance(request, HttpRequest)     
    return render(         
     request,         
     'app/post.html',         
     {                     # параметр в {} – данные для использования в шаблоне.             
       'title':'Блог',   
	   'posts':posts,
       'form': form,                        # передача списка статей в шаблон веб-страницы              
       'year':datetime.now().year,         
     }     
   ) 

def delete(request, parametr, comm):
   post_1 = Blog.objects.get(id=parametr)
   Comment.objects.filter(id=comm).delete()
   return redirect("blogpost" ,parametr=post_1.id)
   return render(         
    request,         
    'app/blogpost.html',         
    {                                                        
      'post_1': post_1,                  # передача конкретной статьи в шаблон веб-страницы                
      'comments': comments,              # передача всех комментариев к данной статье в шаблон веб-страницы              
      'form': form,                      # передача формы в шаблон вебстраницы
   
       'year':datetime.now().year, 
    } 
  )
def deleteBlog(request, parametr):
   post_1 = Blog.objects.filter(id=parametr).delete()
   return redirect("blog" )
   return render(         
    request,         
    'app/blogpost.html',         
    {                                                        
      'post_1': post_1,                  # передача конкретной статьи в шаблон веб-страницы                
      'comments': comments,              # передача всех комментариев к данной статье в шаблон веб-страницы              
      'form': form,                      # передача формы в шаблон вебстраницы
   
       'year':datetime.now().year, 
    } 
  )
def deleteall(request, parametr,offset):
   post_1 = Blog.objects.get(id=parametr) 
   Comment.objects.all().delete()
   return redirect("blogpost" ,parametr=post_1.id)
   return render(         
    request,         
    'app/blogpost.html',         
    {                                                        
      'post_1': post_1,                  # передача конкретной статьи в шаблон веб-страницы                
      'comments': comments,              # передача всех комментариев к данной статье в шаблон веб-страницы              
      'form': form,                      # передача формы в шаблон вебстраницы
   
       'year':datetime.now().year, 
    } 
  )
def cart(request):
    assert isinstance(request, HttpRequest)
    Basket.objects.filter(user=request.user, price=0).delete()
    basket = Basket.objects.filter(user=request.user)
    summ = 0
    for item in basket:
        summ += item.price * item.quantity


    return render(
    request,
    'app/cart.html',
    { 'basket': basket,
    'title':'Блог',
    'year':datetime.now().year,
    'summ':summ,
    }
    )
def deletecart(request, comm):
   
   Comment.objects.filter(id=comm).delete()
   return redirect("cart")
   return render(         
    request,         
    'app/cart.html',         
    {                                                        
                        # передача конкретной статьи в шаблон веб-страницы                
      'comments': comments,              # передача всех комментариев к данной статье в шаблон веб-страницы              
      'form': form,                      # передача формы в шаблон вебстраницы
   
       'year':datetime.now().year, 
    } 
  )   
def additem(request, parametr):
 assert isinstance(request, HttpRequest)
 post_1 = Blog.objects.get(id=parametr)
 obj, created = Basket.objects.get_or_create(user=request.user, item=post_1)
 obj.quantity = obj.quantity + 1
 pr = post_1.description.replace(' ', '')
 obj.price =  int(pr)
 obj.save()  
 return redirect("blogpost" ,parametr=post_1.id)
 return render(         
     request,         
     'app/blogpost.html',         
     {                     # параметр в {} – данные для использования в шаблоне.             
       'title':'Блог',             
       
       'Basket': Basket,  # передача списка статей в шаблон веб-страницы              
       'year':datetime.now().year,         
     }     
   ) 
def news(request):
    assert isinstance(request, HttpRequest)
    news = News.objects.all() # запрос на выбор всех статей блога из модели 
    return render(         
     request,         
     'app/index.html',         
     {                     # параметр в {} – данные для использования в шаблоне.             
       'title':'Блог',             
       'news': news,                         # передача списка статей в шаблон веб-страницы              
       'year':datetime.now().year,         
     }     
   ) 
def basket(request):
    assert isinstance(request, HttpRequest)
    basket = Basket.objects.all() # запрос на выбор всех статей блога из модели 
    return render(         
     request,         
     'app/index.html',         
     {                     # параметр в {} – данные для использования в шаблоне.             
       'title':'Блог',             
       
       'Basket': Basket,  # передача списка статей в шаблон веб-страницы              
       'year':datetime.now().year,         
     }     
   ) 
def newpost (request):
    news = News.objects.all()
    if request.method == "POST":                            # после отправки данных формы на сервер методом POST         
      form = NewsForm(request.POST)         
      if form.is_valid(): 	  
            form.save()                             # сохраняем изменения после добавления полей   
            return redirect('newpost')     # переадресация на ту же страницу статьи после отправки комментария     
    else:                                                    
     form = NewsForm()                                 # создание формы для ввода комментария 
  
    assert isinstance(request, HttpRequest)     
    return render(         
     request,         
     'app/newpost.html',         
     {                     # параметр в {} – данные для использования в шаблоне.             
       'title':'Блог',   
	   'news':news,
       'form': form,                        # передача списка статей в шаблон веб-страницы              
       'year':datetime.now().year,         
     }     
   )
def deletebasket(request, comm):
   
   Basket.objects.filter(id=comm).delete()
   return redirect("cart")
   return render(         
    request,         
    'app/cart.html',         
    {                                                        
                        # передача конкретной статьи в шаблон веб-страницы                
      'basket': basket,              # передача всех комментариев к данной статье в шаблон веб-страницы              
      'form': form,                      # передача формы в шаблон вебстраницы
   
       'year':datetime.now().year, 
    } 
  )

def incrementbasket(request, comm):   
   obj = Basket.objects.get(id=comm)
   obj.quantity += 1
   obj.save()
   return redirect("cart")

def decrementbasket(request, comm):   
   obj = Basket.objects.get(id=comm)
   obj.quantity -= 1
   if obj.quantity == 0:
       obj.delete()
   else:
       obj.save()
   return redirect("cart")