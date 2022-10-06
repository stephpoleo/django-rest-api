from django.urls import path
from .views import FamilyView

urlpatterns = [
    path('family/', FamilyView.as_view(), name= 'family_list'),
    path('family/<int:id>', FamilyView.as_view(), name= 'family_id'),
]