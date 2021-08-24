from django.urls import path
from .views import (
    ScoreprojLookupView, 
    scoreproj_searched_view,
)

app_name = "scoreproj"
urlpatterns = [
    path("", ScoreprojLookupView.as_view(), name="scoreproj-lookup-view"),
    path("searched/", scoreproj_searched_view, name="scoreproj-searched-view")
]