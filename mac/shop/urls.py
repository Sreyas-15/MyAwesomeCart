from django.urls import path
from . import views
urlpatterns = [
    path("", views.index,name="ShopHome"),
    path("about/", views.about,name="aboutus"),
    path("contact/", views.contact,name="contactus"),
    path("tracker/", views.tracker,name="trackparcel"),
    path("search/", views.search,name="search"),
    path("productview/", views.productview,name="productview"),
    path("checkout/", views.checkout,name="checkout"),

]