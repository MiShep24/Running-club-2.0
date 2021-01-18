from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class News(models.Model):
    title = models.CharField('Название', max_length=100)
    mainText = models.TextField('Описание')
    timeDate = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Profile(models.Model):
    DoesNotExist = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateTimeField('Дата рождения')
    birth.strftime("%d %b, %Y")
    megafaculty = models.CharField('Мегафакультет', max_length=30)
    group = models.CharField('Номер группы', max_length=10)
    info = models.TextField('Дополнительная нформация')
    
    def __str__(self):
        return self.user.username

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''