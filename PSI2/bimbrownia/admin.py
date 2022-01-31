from django.contrib import admin
from .models import alcoholCategory, alcohol, Client, Order
# Register your models here.

admin.site.register(alcoholCategory)
admin.site.register(alcohol)
admin.site.register(Client)
admin.site.register(Order)