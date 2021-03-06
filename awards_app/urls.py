from django.urls import path
from awards_app import views

urlpatterns = [
    path("user", views.UserView.as_view(), name="user"),
    path("user/<int:user_id>", views.UserView.as_view(), name="user"),
    path("award", views.AwardView.as_view(), name="award"),
    path("award/<int:award_id>", views.AwardView.as_view(), name="award"),
]
