from django.shortcuts import render

from Aries.views import ApplicationBaseView
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Team_Member
from  .serilizers import TeamMemberSerializer

class TeamMemberView(ApplicationBaseView,ListCreateAPIView):
        allowed_methods = ('GET',)
        
        queryset = Team_Member.objects.all()
        serializer_class = TeamMemberSerializer
    

   