from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import ClientProfileSerializer, OfferSerializer, RequestSerializer, RequestOrganizationSerializer, RequestPartnerSerializer
from api.permissions import ClientProfilePermission, OfferPermission, RequestPermission
from api.models import ClientProfileModel, OfferModel, RequestModel


class ClientProfileList(generics.ListCreateAPIView):
    """
    Вывод всех анкет, добавление новых анкет
    """

    serializer_class = ClientProfileSerializer
    permission_classes = [ClientProfilePermission, ]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        query = ClientProfileModel.objects

        if self.request.user.is_superuser:
            return query.all()

        return query.filter(partner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(partner=self.request.user)


class ClientProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Обновление, удаление экземпляра анкет
    """

    serializer_class = ClientProfileSerializer
    permission_classes = [ClientProfilePermission, ]

    def get_queryset(self):
        query = ClientProfileModel.objects

        if self.request.user.is_superuser:
            return query.all()

        return query.filter(partner=self.request.user)


class OfferList(generics.ListCreateAPIView):
    """
    Вывод всех предложеий
    """

    serializer_class = OfferSerializer
    permission_classes = [OfferPermission, ]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        query = OfferModel.objects

        if self.request.user.groups.filter(name='organization').exists():
            query = query.filter(organization=self.request.user)

        return query.all()


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Вывод экземпляра предложения
    """

    serializer_class = OfferSerializer
    permission_classes = [OfferPermission, ]

    def get_queryset(self):
        query = OfferModel.objects

        if self.request.user.groups.filter(name='organization').exists():
            query = query.filter(organization=self.request.user)

        return query.all()


class RequestList(generics.ListCreateAPIView):
    """
    Вывод всех анкет, добавление новых заявок
    """

    permission_classes = [RequestPermission, ]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.request.user.groups.filter(name='organization').exists():
            return RequestOrganizationSerializer
        elif self.request.user.groups.filter(name='partner').exists():
            return RequestPartnerSerializer

        return RequestSerializer

    def get_queryset(self):
        query = RequestModel.objects

        if self.request.user.is_superuser:
            return query.all()
        elif self.request.user.groups.filter(name='organization').exists():
            return query.filter(offer__organization=self.request.user)

        return query.filter(client_profile__partner=self.request.user)


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Вывод экземпляра заявки
    """

    permission_classes = [RequestPermission, ]

    def get_serializer_class(self):
        if self.request.user.groups.filter(name='organization').exists():
            return RequestOrganizationSerializer

        return RequestSerializer

    def get_queryset(self):
        query = RequestModel.objects

        if self.request.user.is_superuser:
            return query.all()
        elif self.request.user.groups.filter(name='organization').exists():
            return query.filter(offer__organization=self.request.user)

        return query.filter(client_profile__partner=self.request.user)