from django.conf.urls import url
from . import views
app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin_template, name="signin"),
    url(r'^signup/$', views.signup_template, name="signup"),
    url(r'^success/$', views.success, name='success'),
    url(r'^api/signup/$', views.signup, name='api_singup'),
    url(r'^api/signin/$', views.signin, name='api_signin'),
]
