from django.shortcuts import render


def home(request):
    return render(request=request, template_name="main/home.html", context={'message': 'Hello, World!'})
