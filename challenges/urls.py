from django.urls import path
from . import views
urlpatterns = [
    # path("january", views.index),
    # path("february", views.index),
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_num),
    path("<str:month>", views.monthly_challenge, name = "month-challenge"),
]
