from django.http import HttpResponse
def foo(request):
 for k,v in request.GET.items():
  print k,v
 return HttpResponse(request.method)