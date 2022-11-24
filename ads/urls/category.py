from django.urls import path

from ads.views.category import *

urlpatterns = [
    path('', CategoriesListView.as_view()),
    path('<int:pk>/', CategorySingleView.as_view()),
    path('create/', category_create_view),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view())

]