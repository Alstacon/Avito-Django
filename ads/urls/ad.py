from django.urls import path

from ads.views.ad import *

urlpatterns = [
    # path('', views.AdsListView.as_view()),
    # path('<int:pk>/', views.AdSingleView.as_view()),
    # path('create/', views.AdCreateView.as_view()),
    # path('<int:pk>/update/', views.AdUpdateView.as_view()),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view()),
    # path('<int:pk>/delete/', AdDeleteView.as_view()),

]