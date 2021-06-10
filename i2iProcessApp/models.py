from django.db import models
from django.core import validators


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='name',unique=True)
    passward = models.CharField(max_length=20,verbose_name='password',validators=[validators.MinLengthValidator(6,message='not less than 6')])
    registe_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    '''
    class Meta:
        db_table = 'user'
        ordering = ['id']
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
    '''

class admin(User):
    admin_id = models.IntegerField(verbose_name='id',primary_key=True)
    Authorization = models.IntegerField(verbose_name='authorization')

    def getAuthorization(self):
        return self.Authorization

class client(User):
    client_id = models.IntegerField(verbose_name='id',primary_key=True)
    history = models.TextField()

    def getHistory(self):
        return self.history

class Img(models.Model):
    name = models.CharField(max_length=64)
    uploader = models.CharField(max_length= 32)
    add_time  = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=128)
    