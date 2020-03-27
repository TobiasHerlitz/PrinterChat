from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
import time

from main_app.models import Message


# Create your views here.
class Index(LoginRequiredMixin, CreateView):
	login_url = 'Login'
	template_name = 'index.html'

	fields = ['text_content']
	model = Message

	def form_valid(self, form):
		message_instance = form.save(commit=False)
		message_instance.poster = User.objects.get(first_name=self.request.user)
		message_instance.timestamp = time.strftime('%d-%b %H:%M')
		message_instance.save()
		return HttpResponseRedirect('/')

	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context["all_objects"] = self.model.objects.all()
		context["last_four_objects"] = context["all_objects"][len(context["all_objects"])-4:len(context["all_objects"]):1]
		return context

class Login(LoginView):
	template_name = 'login.html'

class Logout(LogoutView):
	pass

class SendMessage(LoginRequiredMixin, CreateView):
	login_url = 'Login'
	template_name = 'sendmessage.html'

	model = Message
	fields = ['text_content']

	def form_valid(self, form):
		message_instance = form.save(commit=False)
		message_instance.poster = User.objects.get(first_name=self.request.user)
		message_instance.timestamp = time.strftime('%d-%b %H:%M')
		message_instance.save()
		return HttpResponseRedirect('/')


class ShowMessages(LoginRequiredMixin, ListView):
	login_url = 'Login'
	template_name = 'showmessages.html'
	model = Message