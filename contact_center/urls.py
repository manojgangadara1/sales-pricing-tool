from django.urls import path
from .views import landing_page
from . import views

urlpatterns = [
    path('', landing_page, name='contact_landing'),  # This will serve the landing page at /contact_center/
    path('webex_contact_center/', views.webex_contact_center, name='webex_contact_center'),
]
