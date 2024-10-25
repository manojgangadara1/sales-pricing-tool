from django.shortcuts import render

def sip_trunk_home(request):
    return render(request, 'sip_trunk/home.html')  # Render SIP Trunk template
