from accounts.models import UserProfile, EmailActivation, Following
from django.contrib import admin

admin.site.register(UserProfile)
admin.site.register(EmailActivation)
admin.site.register(Following)