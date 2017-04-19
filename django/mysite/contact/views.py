from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/concent/thanks/')
    else:
        form = ContactForm(
            initial={'subject':'I lobe your site!'}
        )
    return render_to_response('contact_form.html',{'form':form})