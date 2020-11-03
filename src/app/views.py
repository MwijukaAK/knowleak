from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
import requests, json
from app.models import Reading

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
	template_name ='pages/dashboard.html'
	login_url = 'login'

class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'pages/profile.html'
	login_url = 'login'

class ReportView(LoginRequiredMixin, ListView):
	model = Reading
	template_name = 'pages/reports.html'
	login_url= 'login'

	def get_queryset(self):
		return Reading.objects.order_by('-id')


class NotificationView(LoginRequiredMixin,TemplateView):
	template_name ='pages/notifications.html'
	login_url = 'login'
