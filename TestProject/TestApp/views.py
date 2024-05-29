from django.shortcuts import render

# Create your views here.
def TestApp(request):
    return render(request, "home.html", status=200)