from django.contrib import admin

# Register your models here.
from .models import question,answer,user

admin.site.register(question)
admin.site.register(answer)
admin.site.register(user)