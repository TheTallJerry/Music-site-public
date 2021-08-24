from django.urls import path
from .views import (
    dynamic_lookup_view, 
    score_home_view, 
)

app_name = "scores"
urlpatterns = [
    path('<int:id>/', dynamic_lookup_view, name='score-details'),
    path('', score_home_view, name='score-home'),]