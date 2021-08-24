from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist
from .forms import ContactRequestForm
from .models import ContactRequest
from .sendemail import send_email

import datetime

def contact_home_view(request):
    return render(request, "contact/contact_home.html", None)

# creates a request and sends an email to my designated email account

def contact_req_lookup_view(request):
    if request.method == "POST":   
        try:
            id_ = request.POST.get("search")
            obj = ContactRequest.objects.get(id=id_)
        except ValueError: 
            return render(request, "invalid_input.html", {})
        except ObjectDoesNotExist:
            return render(request, "contact/contact_req_not_exist.html", {})
        context = {
            "id": id_, 
            "resolved": obj.resolved, 
            "commentFromAdmin": obj.commentFromAdmin
        }
        return render(request, "contact/contact_req_disp.html", context)
    else:
        return render(request, "invalid_input.html", {})

class ContactRequestCreateView(CreateView):
    template_name = 'contact/contact_request.html'
    form_class = ContactRequestForm
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ContactRequest, id=id_)
        
    # not having this html as another path because i don't want people mannually accessing it
    def form_valid(self, form) -> HttpResponse:
        # don't save just yet
        task = form.save(commit=False)
        context = {
            "name": form.cleaned_data["name"], 
            "subject": form.cleaned_data["subject"], 
            "comments": form.cleaned_data["comments"], 
            "email": form.cleaned_data["email"],
            "title": form.cleaned_data["title"], 
            "time": str(datetime.date.today()),
            "id": len(ContactRequest.objects.all()) + 1}
        # if the email was sent succesfully, redirect to success page; else redirect to failure page
        if send_email(context):
            task.save()
            return render(self.request, "contact/contact_request_success.html", context)
        return render(self.request, "contact/fail_to_send_email.html", context)
