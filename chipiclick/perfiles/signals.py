__author__ = 'juan'

from  chipiclick.perfiles.models import  Perfil
from django.contrib.auth.models import User
from django.db.models.signals import post_save

    #Make sure we create a FacebookProfile when creating a User
def create_facebook_profile(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)

