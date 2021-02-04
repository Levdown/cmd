from django.contrib import admin

# Register your models here.

from .models import Coin 

admin.site.register(Coin)

# @admin.register(Coin)
# class AdminCoin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'symbol', 'price', 'rank', 'image')