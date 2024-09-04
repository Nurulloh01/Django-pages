from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('services/', views.ServicesPageView.as_view(), name='services'),
    path('news/', views.NewsPageView.as_view(), name='news'),
    # other paths
]
