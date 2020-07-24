from django.contrib import admin

from .models import question,user,answer

# Register your models here.
admin.site.register(question)
admin.site.register(user)
admin.site.register(answer)