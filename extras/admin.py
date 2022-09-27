from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(Blog)
admin.site.register(Faq)
admin.site.register(Testemonial)
admin.site.register(Research)

