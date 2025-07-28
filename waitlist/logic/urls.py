from django.urls import path
from . import views

urlpatterns = [
    path('', views.waitlist_signup_view, name='waitlist_signup'),
    path('success/', views.success_page_view, name='success_page'),
]
