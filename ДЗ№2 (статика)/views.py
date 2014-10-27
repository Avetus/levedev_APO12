from django.shortcuts import render_to_response
from django.http import HttpResponse

def foo(request):
      return render_to_response('index.html')
	  
def login(request):
      return render_to_response('login.html')
	  
def signup(request):
      return render_to_response('signup.html')