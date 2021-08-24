from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from.models import Score
# Create your views here.

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Score, id=id)
    context = {"object": obj}
    return render(request, "score/score_details.html", context)

def score_home_view(request):
    res = Score.objects.all()
    context = {"object_list": res}
    return render(request, "score/score_home.html", context)
    
def score_truth_view(request):
    return render(request, "score/score_descriptions/truth.html", {})

def score_mst_view(request):
    return render(request, "score/score_descriptions/march_of_the_steel_torrent.html", {})