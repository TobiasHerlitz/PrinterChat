from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from main_app.models import Message
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
class Index(TemplateView):
	template_name = 'index.html'

class TestPage(TemplateView):
	template_name = 'testpage.html'

class Login(LoginView):
	template_name = 'login.html'

class Logout(LogoutView):
	pass

class SendMessage(CreateView):
	template_name = 'sendmessage.html'
	model = Message
	fields = ['text_content']

class ShowMessages(ListView):
	template_name = 'showmessages.html'
	model = Message
