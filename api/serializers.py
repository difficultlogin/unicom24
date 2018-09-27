from rest_framework import serializers
from api.models import OfferModel, ClientProfileModel, RequestModel


class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfileModel
        fields = ('id', 'first_name', 'last_name',  'middle_name',  'birthday',  'phone',  'passport_id',
                  'scoring_score')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferModel
        fields = ('id', 'name', 'offer_type', 'scoring_score_min', 'scoring_score_max', 'rotation_start', 'rotation_end',
                  'organization')


class ClientProfileField(serializers.PrimaryKeyRelatedField):
    """
    Диначеское поле анкеты для партнеров
    """

    def get_queryset(self):
        user = self.context['request'].user
        return ClientProfileModel.objects.filter(partner=user)


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'


class RequestPartnerSerializer(serializers.ModelSerializer):
    client_profile = ClientProfileField()
    status = serializers.CharField(read_only=True)

    class Meta:
        model = RequestModel
        fields = '__all__'


class RequestOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
            'client_profile': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'offer': {'read_only': True},
        }