from django.shortcuts import render

# Create your views here.
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
        print("HI")
        return render(request, 'homeapp/contact.html')
        
    except:
        print("BY")
        return render(request, '404.html',status=404)