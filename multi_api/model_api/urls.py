from django.urls import path
from .views import BurgerListCreateView, BurgerDetailView

urlpatterns = [
    path('burgers/', BurgerListCreateView.as_view(), name='burger-list'),
    path('burgers/<int:pk>/', BurgerDetailView.as_view(), name='burger-detail'),

]
