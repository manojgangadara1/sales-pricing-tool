from django.shortcuts import render

def landing_page(request):
    return render(request, 'unified_communications/landing_page.html')

def home_view(request):
    return render(request, 'unified_communications/home.html')  # This line should match your directory structure

def webex_calling_wholesale(request):
    return render(request, 'unified_communications/webex_calling_wholesale.html')

def webex_calling_flex(request):
    return render(request, 'unified_communications/webex_calling_flex.html')

def on_prem_ucm_hybrid(request):
    return render(request, 'unified_communications/on_prem_ucm_hybrid.html')