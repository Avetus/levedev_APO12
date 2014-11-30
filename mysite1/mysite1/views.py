import csv
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from polls.models import Question

def foo(request, sort='new'):
	limit = 5
	pager = Paginator(queryset, limit)
	page = request.GET.get('page', 1)
	try:
	context['Question'] = pager.page(page).object_list
	except EmptyPage:
		raise Http404
	context['pager'] = pager
    return render(request, 'index.html', context)
	  
def login(request):
    return render(request, 'login.html')
	  
def signup(request):
    return render(request, 'signup.html')
	
def generate_user(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="user.csv"'
	writer = csv.writer(response)
	for i in range(10000)
		writer.writerow([i, i+'username', i+'@mail.ru', '2014-11-9', 0])
    return response
	
def generate_tag(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="tag.csv"'
	writer = csv.writer(response)
	for i in range(100)
		writer.writerow([i, 'newtag'+i])
    return response

def generate_question(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="question.csv"'
	writer = csv.writer(response)
	for i in range(100000)
		writer.writerow([i, i+'username', '2014-11-9', 1, 1, 0])
    return response

def generate_answer(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="answer.csv"'
	writer = csv.writer(response)
	for i in range(1000000)
		writer.writerow([i, i+'username', '2014-11-9', 1, 1, 0])
    return response