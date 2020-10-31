from django.db import models
from django.contrib.auth.models import User, Permission, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import permission_required
# Create your models here.

class Tasks(models.Model):


    assigner = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    dateon = models.DateField()
    duedate = models.DateField()
    status = models.BooleanField(default=True)


#class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #level = models.CharField(max_length=2)


#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
    #instance.profile.save()