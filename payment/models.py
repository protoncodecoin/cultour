from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

import secrets

from rest_framework import serializers
from payment.paystack import Paystack
from users.models import Tourist


# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(Tourist, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return f"Payment: ${self.amount}"

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref

        super().save(*args, **kwargs)

    def amount_value(self):
        return int(self.amount) * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

    @staticmethod
    def get_content_type(model_name: str):
        try:
            content_type = ContentType.objects.get(model=model_name.lower())
        except ContentType.DoesNotExist:
            raise serializers.ValidationError({"model": "Invalide model name"})

        return content_type


# @classmethod
# def convert_content_type(cls, model_name: str):
#     try:
#         content_type = ContentType.objects.get(model=model_name.lower())
#     except ContentType.DoesNotExist:
#         raise serializers.ValidationError({"model": "Invalide model name"})
