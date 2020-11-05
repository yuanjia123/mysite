from django.urls import path
from polls.views import LoginView,Test_View,SendSmsView
from django.conf.urls import url

#取消csrf_token的工具
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', LoginView.as_view(),name='index'),
    path('test/', Test_View.as_view(),name='test'),
    path('send_sms',csrf_exempt(SendSmsView.as_view()),name="send_sms"), #接受验证码的 接口
]