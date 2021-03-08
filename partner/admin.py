from django.contrib import admin
from .models import Category, Partner, SocialNetwork
# Register your models here.

admin.site.register(Partner)
admin.site.register(Category)
admin.site.register(SocialNetwork)