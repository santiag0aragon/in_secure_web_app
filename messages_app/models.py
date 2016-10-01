import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class NotificationUser(models.Model):
    """
    Model to represent messages between users.
        viewed: If True the message is not displayed
        user: The message's receiver
        author: The message's author
    """
    title = models.CharField(max_length=256, blank=False)
    message = models.TextField(blank=False)
    viewed = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.now(),
                            blank=False)
    user = models.ForeignKey(User, blank=False)
    author = models.ForeignKey(User, blank=False, null=True,
                               related_name='author')

    def __unicode__(self):
        return str(self.title)


@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
    if kwargs.get("created", False):
        NotificationUser.objects.create(
                user=kwargs.get("instance"),
                title="Welcome to ",
                message="Test message.")
