from django.shortcuts import render

def switches_home(request):
    return render(request, 'switches/home.html')  # Render Switches template
