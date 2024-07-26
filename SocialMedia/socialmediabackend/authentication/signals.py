from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Notification
import json

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tasks import send_activation_email

@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        notification_obj = Notification.objects.filter(
            is_seen=False, user=instance.user
        )
        user_id = str(instance.user.id)
        data = {"notifications": notification_obj}

        async_to_sync(channel_layer.group_send)(
            user_id, {"type": "send_allNotification", "value": json.dumps(data)}
        )


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        uid = urlsafe_base64_encode(force_bytes(instance.pk))
        token = default_token_generator.make_token(instance)
        activation_link = f"https://konnectify.info/activate/{uid}/{token}"
        send_activation_email.delay(instance.email, activation_link)
