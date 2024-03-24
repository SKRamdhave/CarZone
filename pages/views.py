from django.shortcuts import render

# Create your views here.

# `page` app - view function
def home(request):
    return render(request, 'pages/home.html')