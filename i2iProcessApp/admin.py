from django.contrib import admin

# Register your models here.
from i2iProcessApp import models

admin.site.register(models.admin)
admin.site.register(models.client)
admin.site.register(models.Img)
