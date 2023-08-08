from django.urls import path
from .views import TeamMemberView 

urlpatterns = [
    path('team/', TeamMemberView.as_view()),
]