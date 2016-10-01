# # # -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class WeakUser(models.Model):
    """
    Object class extention of the User model.
        user: mapping to User model
        weak_pwd: stored plaintext password to perform auth.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='user',
        blank=False
    )
    weak_pwd = models.CharField(
        max_length=50,
        verbose_name='weak password',
        blank=True
    )

    def __unicode__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Weak User'
        verbose_name_plural = 'Weak Users'
