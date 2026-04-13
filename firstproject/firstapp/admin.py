from django.contrib import admin
from .models import Member, Reservation

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date")

admin.site.register(Member, MemberAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "guest_count", "reservation_time", "comments")
    
admin.site.register(Reservation, ReservationAdmin)