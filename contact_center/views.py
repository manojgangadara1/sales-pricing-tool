from django.shortcuts import render

def landing_page(request):
    return render(request, 'contact_center/landing_page.html')
def webex_contact_center(request):
    return render(request, 'contact_center/webex_contact_center.html')