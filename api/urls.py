from django.urls import re_path

from api import views


urlpatterns = [
    re_path(r'^clients/$', views.ClientProfileList.as_view(), name='api-clients'),
    re_path(r'^clients/(?P<pk>[0-9]+)/$', views.ClientProfileDetail.as_view()),
    re_path(r'^offers/$', views.OfferList.as_view()),
    re_path(r'^offers/(?P<pk>[0-9]+)/$', views.OfferDetail.as_view()),
    re_path(r'^requests/$', views.RequestList.as_view(), name='api-requests'),
    re_path(r'^requests/(?P<pk>[0-9]+)/$', views.RequestDetail.as_view())
]