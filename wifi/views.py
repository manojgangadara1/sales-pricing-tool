from django.shortcuts import render

def wifi_home(request):
    return render(request, 'wifi/home.html')  # Render WiFi template
