from django.contrib import admin
from django.urls import path, include
from unified_communications.views import home_view  # Import the home view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Route for the home page
    path('contact_center/', include('contact_center.urls')),  # Include contact_center URLs
    path('unified_communications/', include('unified_communications.urls')),  # Include unified_communications URLs
    path('sdwan/', include('sdwan.urls')),  # SDWAN
    path('switches/', include('switches.urls')),  # Switches
    path('wifi/', include('wifi.urls')),  # WiFi
    path('sip_trunk/', include('sip_trunk.urls')),  # SIP Trunk
]
