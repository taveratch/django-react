from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from django.core.context_processors import csrf
from django.views.decorators import csrf
from react.render import render_component
from .models import User
import django.contrib.auth as auth
import os
# Create your views here.

def index(request):
    return HttpResponse('Index')

def signup_template(request):
    rendered = render_component(os.path.join(os.getcwd()+'/login/static/js/login/signup.jsx'),
        {'token': str(getTokenTemplate(request))},
        to_static_markup=False)
    return render(request, 'index.html', {'component': rendered})


def signin_template(request):
    rendered = render_component(os.path.join(os.getcwd()+'/login/static/js/login/signin.jsx'),
        {'token': str(getTokenTemplate(request))},
        to_static_markup=False)
    return render(request, 'index.html', {'component': rendered})

def success(request):
    print(request)
    return HttpResponse("login successful")

def getTokenTemplate(request):
    return render(request, 'token.html', {}).content


# ==== API ====
def signup(request):
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm-password']
    if(password != confirm_password):
        return HttpResponseRedirect(reverse('login:signup'))
    if(isUserExist(email)):
        return HttpResponse('User already exist')
    else:
        a = User(email=email, password=password)
        a.save()
        return HttpResponse('Welcome %s' % (a.__str__()))

def signin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authorizeUser(email, password)
    if (user == False):
        return HttpResponseRedirect(reverse('login:signin'))
    else:
        # auth_user = auth.authenticate(email=email, password=password)
        # auth.login(request, auth_user)
        return HttpResponseRedirect(reverse('login:success'))

def isUserExist(email):
    for user in User.objects.all():
        if(user.email == email):
            return True
    return False

def authorizeUser(email, password):
    for user in User.objects.all():
        if(user.email == email and user.password == password):
            return user
    return False
