from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
#from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


def login(request):
	return render_to_response('templates/index.html')#, c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('loggedin')
	else:
		return HttpResponseRedirect('invalid_login')

def loggedin(request):
	return render_to_response('loggedin.html', 'full_name': request.user.username)

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')