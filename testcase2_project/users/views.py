from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
	users = User.objects.all().values()
	template = loader.get_template('all_users.html')
	context = {
		'users': users
	}
	return HttpResponse(template.render(context, request))