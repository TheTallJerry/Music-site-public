from django.shortcuts import render
from message.models import Message
from utils.scrap import get_best_comment


def home_view(request):
    raw_query = "select * from message_Message order by id limit 1"
    object = Message.objects.raw(raw_query)
    if not object: 
        context = {"object": None}
    else:
        context = {"object": object[0]}
    try:
        s = get_best_comment()
    except:
        s = None
    context["test"] = s
    return render(request, "home.html", context)
    
def honorablementions_view(request):
    return render(request, "honorablementions.html", {})