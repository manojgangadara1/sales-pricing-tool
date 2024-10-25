from django.urls import path
from .views import landing_page
from . import views

urlpatterns = [
    path('', landing_page, name='unified_landing'),  # This will serve the landing page at /unified_communications/
    path('webex_calling_wholesale/', views.webex_calling_wholesale, name='webex_calling_wholesale'),
    path('webex_calling_flex/', views.webex_calling_flex, name='webex_calling_flex'),
    path('on_prem_ucm_hybrid/', views.on_prem_ucm_hybrid, name='on_prem_ucm_hybrid'),
]
