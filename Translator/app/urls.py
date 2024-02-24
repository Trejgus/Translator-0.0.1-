from django.urls import path
from . import api, views

urlpatterns = [
    path('', views.translator_page, name = 'translator_page'),
    # api
    path('api/v1/translate/<str:text>/<str:to_lang>/', api.APITranslate.as_view()),
    path('api/v1/translate/<str:text>/<str:to_lang>/<str:translator>/', api.APITranslate.as_view()),
    # path('api/v1/translate/<str:text>/<str:to_lang>/<str:translator>'),
]
