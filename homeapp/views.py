from django.shortcuts import render
# Create your views
def index(request):
    try:
        return render(request, 'homeapp/index.html')
    except:
        return render(request, '404.html',status=404)

def about(request):
    try:
        return render(request, 'homeapp/about.html')
    except:
        return render(request, '404.html',status=404)

def contact(request):
    try:
        return render(request, 'homeapp/contact.html')
        
    except:
        return render(request, '404.html',status=404)