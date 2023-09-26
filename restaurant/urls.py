from django.urls import path
from . import views

urlpatterns = [
    path("", views.MenuList.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("item/<int:pk>/", views.MenuItemDetails.as_view(), name="menu_item"),
]
