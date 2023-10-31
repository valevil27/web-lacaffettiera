from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.
def contact(request):
    form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            # If everything goes well, redirect
            email = EmailMessage(
                subject= "La Caffettiera: Mensaje de Contacto",
                body= f"De: {name} <{email}> \n\n{content}",
                from_email= "no-reply@inbox.mailtrap.io",
                to= ["tehvalero@gmail.com"],
                reply_to= [email]
            )
            try:
                email.send()
            except:
                return redirect(reverse("contact") + "?fail")
                
            return redirect(reverse("contact") + "?ok")
    return render(request, "contact/contact.html", {"form": form})
