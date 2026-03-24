from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # خزّن الرسالة أولاً
        msg = ContactMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject="New Contact Message",
            message=message,
        )

        subject = f"New Contact Message #{msg.id}"

        email_body = (
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )

        email_msg = EmailMessage(
            subject=subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=getattr(settings, "CONTACT_RECEIVERS", []),
            reply_to=[email] if email else None,
        )
        email_msg.send(fail_silently=False)

        return redirect("contact")

    return render(request, "contact/contact.html")
