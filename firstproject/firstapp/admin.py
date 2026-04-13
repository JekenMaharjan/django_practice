from django.contrib import admin
from .models import Member, Reservation

# Register your models here.
admin.site.register(Member)
admin.site.register(Reservation)