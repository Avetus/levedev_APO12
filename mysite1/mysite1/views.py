from django.http import HttpResponse
def params(request):
    output = 'Hello, world!<br><br>'
    
    if request.method == 'GET':
        output += 'GET:'
        get_query = request.GET
        for key in get_query:
            output += '<br>' + key + ' = ' + get_query[key]
    elif request.method == 'POST':
        output += '<br>POST:<br>'
        post_query = request.POST
        for key in post_query:
            output += '<br>' + key + ' = ' + post_query[key]
    return HttpResponse(output)
