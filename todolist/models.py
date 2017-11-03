from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Tasklist(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User,
                              related_name='tasklists',
                              on_delete=models.CASCADE)
    sharers = models.ManyToManyField(User, related_name='shared_tasklists')

    def __str__(self):
        return "{}".format(self.name)


class TaskTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class Task(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    tasklist = models.ForeignKey(Tasklist,
                                 related_name='tasks',
                                 on_delete=models.CASCADE)
    tags = models.ManyToManyField(TaskTag)

    PRIORITY = (
        ('h', 'High'),
        ('m', 'Medium'),
        ('l', 'Low'),
        ('n', 'None')
    )

    priority = models.CharField(max_length=1, choices=PRIORITY, default='n')

    def __str__(self):
        return "{}".format(self.name)
