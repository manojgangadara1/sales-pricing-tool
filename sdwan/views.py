from django.shortcuts import render

def sdwan_home(request):
    return render(request, 'sdwan/home.html')  # Render SDWAN template
