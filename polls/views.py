from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from polls.forms import Acquire


class Test_View(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'test.html')

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'index.html')

class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        a_form = Acquire(request.POST)
        if a_form.is_valid():
            username = a_form.cleaned_data['username']
            print('----------在这里看模板给视图发送的json（jaxa）数据---------',username)



