from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>This is Home page|back button and hyperlink </h1>')
def index(request):
    return HttpResponse('<h1><a href="https://www.facebook.com" target="_blank">Open Facebook</a></h1>')
def book(request):
    return HttpResponse("book page <a href='/'>Back</a>")