
from django.contrib import admin
from django.urls import path

from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('cat/', views.Categories.as_view()),
    path('ad/', views.Ads.as_view()),
    path('cat/<int:pk>/', views.CategorySingle.as_view()),
    path('ad/<int:pk>/', views.AdSingle.as_view()),
]
