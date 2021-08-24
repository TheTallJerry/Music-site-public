from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email(context: dict):
    subject = "Confirmation of request from {} {}".format(context["title"], context["name"])
    html_msg = render_to_string("contact/email_content.html", context)
    plain_msg = strip_tags(html_msg)
    
    # I only want the email to be sent to the admin account if the request's email is valid
    if send_mail(subject, plain_msg, EMAIL_HOST_USER, [context["email"]], html_message=html_msg) == 1:
        send_mail(subject, plain_msg, EMAIL_HOST_USER, [EMAIL_HOST_USER], html_message=html_msg)
        return True
    return False