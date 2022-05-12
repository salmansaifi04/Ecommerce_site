from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='shophome'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("tracker/", views.tracker, name='tracker'),
    path("search/", views.search, name='search'),
    path("product/<int:myid>/", views.productview, name='product'),
    path("checkout/", views.checkout, name='check'),
]
