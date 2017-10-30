#! /usr/bin/env python
# -*- coding: utf-8
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from douban.models import MovieStar,Starring
from rest_framework import viewsets
from douban.serializers import UserSerializer,GroupSerializer,MovieSerializer,StarringSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API端：允许查看和编辑组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieStar.objects.all()
    serializer_class = MovieSerializer

class StarringViewSet(viewsets.ModelViewSet):
    queryset = Starring.objects.all()
    serializer_class = StarringSerializer





