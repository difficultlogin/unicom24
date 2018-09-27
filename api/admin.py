from django.contrib import admin
from api.models import OfferModel, ClientProfileModel, RequestModel


class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'offer_type', 'scoring_score_min', 'scoring_score_max', 'rotation_start', 'rotation_end',
                    'organization', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fields = ('name', 'offer_type',
              ('scoring_score_min', 'scoring_score_max'),
              ('rotation_start', 'rotation_end'), 'organization'
              )
    raw_id_fields = ('organization',)
    list_filter = ('organization', 'rotation_end')
    search_fields = ('name',)


class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'birthday', 'phone', 'passport_id', 'scoring_score',
                    'partner', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fields = (('first_name', 'last_name', 'middle_name'), 'birthday', 'phone', 'passport_id', 'scoring_score', 'partner')
    raw_id_fields = ()
    list_filter = ('partner', )
    search_fields = ('passport_id',)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('client_profile', 'offer', 'status')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fields = ('client_profile', 'offer', 'status')
    list_filter = ('client_profile', 'offer', 'status')
    search_fields = ('client_profile__last_name', 'client_profile__first_name')


admin.site.register(OfferModel, OfferAdmin)
admin.site.register(ClientProfileModel, ClientProfileAdmin)
admin.site.register(RequestModel, RequestAdmin)