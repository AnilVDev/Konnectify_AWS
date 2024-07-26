from celery import shared_task
from django.core.mail import send_mail
from socialmediabackend import settings
from .models import User


@shared_task
def send_follow_notification_email(follower_id, followed_id):
    try:
        follower = User.objects.get(id=follower_id)
        followed = User.objects.get(id=followed_id)
        follower_url = f"https://konnectify.info/{follower.username}"
        subject = "New Follower Notification"
        message = f"Hello {followed.first_name} {followed.last_name},\n\nYou have a new follower: {follower.first_name} {follower.last_name}.\nFollow back: {follower_url}"
        recipient_list = [followed.email]
        sender_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender_email, recipient_list)
    except User.DoesNotExist:
        # Handle the case if either follower or followed user does not exist
        pass


@shared_task
def send_activation_email(email, activation_link):
    subject = "Activate your account"
    message = f"Please click the following link to activate your account:\n\n{activation_link}"
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
