from django.db import models
from django.conf import settings


class OfferModel(models.Model):
    OFFER_TYPE = (
        (1, 'Потребительский'),
        (2, 'Ипотека'),
        (3, 'Автокредит')
    )

    name = models.CharField(max_length=255)
    offer_type = models.SmallIntegerField(choices=OFFER_TYPE)
    scoring_score_min = models.IntegerField()
    scoring_score_max = models.IntegerField()
    rotation_start = models.DateTimeField()
    rotation_end = models.DateTimeField()
    organization = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ClientProfileModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField()
    phone = models.CharField(max_length=11)
    passport_id = models.CharField(max_length=10)
    scoring_score = models.IntegerField(default=0)
    partner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class RequestModel(models.Model):
    REQUEST_STATUS = (
        (1, 'новая'),
        (2, 'отправлена'),
        (3, 'получена'),
        (4, 'одобрено'),
        (5, 'отказано'),
        (6, 'выдано')
    )

    client_profile = models.ForeignKey(ClientProfileModel, on_delete=models.CASCADE)
    offer = models.ForeignKey(OfferModel, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=REQUEST_STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status)