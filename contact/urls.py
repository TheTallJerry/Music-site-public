from django.urls import path
from .views import (
    ContactRequestCreateView, 
    contact_home_view,
    contact_req_lookup_view, 
)

app_name = "contact"
urlpatterns = [
    path("request", ContactRequestCreateView.as_view(), name="contact-request-view"), 
    path("request/search_res", contact_req_lookup_view, name="contact-request-searched-view"), 
    path("", contact_home_view, name="contact-home-view"),
]