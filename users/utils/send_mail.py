from django.core.mail import send_mail
from django.conf import settings


def send_availability_email(name, email, date_from, date_to, guests, children):
    subject = "Availability Request Confirmation"
    message = f"""
Hello {name},

Thank you for reaching out to us with your availability request.

Here are the details we have received:

- Check-in Date: {date_from}
- Check-out Date: {date_to}
- Number of Guests: {guests}
- Number of Children: {children}

We will review your request and get back to you shortly with availability and pricing details.

If you have any questions or need to make changes to your request, feel free to reply to this email.

Best regards,
{settings.SITE_NAME} Team
"""
    send_mail(
        subject,
        message.strip(),
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
