from django.urls import path

from.views import (
    img_filters,
)

urlpatterns = [
    path('filters', img_filters, name="img_filters"),
]