### | Daily Workshop |

##### 사용자인증/사용자권한관리

1. 아래의 회원가입 페이지는 django.contrib.auth.forms 안에 있는 UserCreationForm()을 활용한 것이다. 아래 페이지를 위한 view, url, template을 작성하세요.

   ```python
   # view
   from django.shortcuts import render, redirect
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib.auth import login as auth_login
   
   # Create your views here.
   def signup(request):
       if request.user.is_authenticated:
           return redirect('boards:index')
           
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               user = form.save()             
               auth_login(request, user)      
               return redirect('boards:index')
       else:
           form = UserCreationForm()
       context = {'form': form}
       return render(request, 'accounts/signup.html', context)
   ```

   ```python
   # url
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   
   urlpatterns = [
   	path('signup/', views.signup, name='signup'),
   ]
   ```

   ```html
   <!-- template -->
   {% extends 'boards/base.html' %}
   {% block body %}
   {% load crispy_forms_tags %}
   <h1>회원가입</h1>
   <form action="" method="POST">
       {% csrf_token %}
       {{ form|crispy }}
       <input type="submit" value="Submit"/>
   </form>
   {% endblock %}
   ```

   

