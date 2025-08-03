from django.conf import settings
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages


from django.core.mail import EmailMessage, send_mail

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str

from users.models import Tourist

from .token import generate_token

from django_countries import Countries


User = get_user_model()


# Create your views here.
def user_login(request):
    # check if the HTTP request method is post
    if request.method == "POST":
        # username = request.POST.get("username")
        username = request.POST.get("username")
        password = request.POST.get("password1")

        # check if a user is with the provided email exist
        user_obj = User.objects.filter(username=username).first()
        if not user_obj:

            # Display an error message  if the user does not exist
            messages.error(request, "Invalid credentials Provided")
            return redirect("users:login")

        # Authenticate the user with the provided email
        user = authenticate(
            username=user_obj.username, email=user_obj.email, password=password
        )

        if user is None:
            # Display an error message
            messages.error(request, "Invalid credential provided")
            return redirect("users:login")
        else:
            # log in the use and redirect the user to the dashboard
            login(request, user)
            messages.success(request, "login was succesful")
            return redirect("tours:tours")
    return render(request, "users/login.html", {"selection": "login"})


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")
        # country = request.POST.get("country")

        # # validate username and email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("users:signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("users:signup")

        # validate password
        if password != password2:
            messages.error(request, "Passwords do not match😑")
            return redirect("users:signup")

        # create use object
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()

        # send welcome email
        subject = "Welcome to cultour."
        message = f"Hello {new_user.username}👋😎.\n\nThank you for joining the amazing creative community👪. Please confirm your email address to activate your account.\n\nRegards,\nTeam cultour"
        from_email = settings.EMAIL_HOST_USER
        to_list = [new_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # send email confirmation link
        current_site = get_current_site(request)
        email_subject = "Confirm Your Email Address!"
        token = generate_token.make_token(new_user)
        print(token)
        messages2 = render_to_string(
            "users/email_confirmation.html",
            {
                "name": new_user.username,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                "token": token,
            },
        )

        email = EmailMessage(
            email_subject,
            messages2,
            settings.EMAIL_HOST_USER,
            [new_user.email],
        )
        # send_mail(email_subject, messages2, from_email, to_list, fail_silently=True)
        email.content_subtype = "html"  # Set content type to HTML
        email.send(fail_silently=True)

        messages.success(
            request,
            "Your account has been created successfully🥳🎊! Please check your email to confirm your email address and activate your account.",
        )
        return redirect("users:login")
    return render(request, "users/register.html", {"selection": "signup"})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        new_user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        new_user = None

    if new_user is not None and generate_token.check_token(new_user, token):
        new_user.is_active = True
        new_user.save()
        # Create user Profile
        tourist = Tourist.objects.create(user=new_user)
        tourist.is_active = True
        tourist.save()
        login(request, new_user)
        messages.success(
            request,
            "Your account has been activated!\n\nCheck your Profile to Update it and have Fun🎉🎉🍾.",
        )
        return redirect("users:login")
    else:
        return render(request, "users/activation_failed.html")


def user_logout(request):
    logout(request)
    return redirect("users:login")


def dashboard(request):
    return render(request, "users/dashboard.html")
