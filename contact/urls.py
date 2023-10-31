from django.urls import path
from contact import views

urlpatterns = [
    #! path
    path("", views.contact, name="contact")
]
