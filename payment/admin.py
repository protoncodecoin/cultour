from django.contrib import admin

from .models import Payment

# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id", "ref", "amount", "verified", "date_created"]
    list_filter = ["verified", "date_created"]
