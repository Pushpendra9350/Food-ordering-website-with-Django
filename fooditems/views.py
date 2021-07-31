from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        print("HI")
        return render(request, 'fooditems/index.html')
        
    except:
        print("BY")
        return render(request, '404.html',status=404)

