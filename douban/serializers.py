#! /usr/bin/env python
# -*- coding: utf-8

from django.contrib.auth.models import User, Group
from .models import MovieStar,Starring
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):  #使用了超链接关系（hyperlinked relations），借助的类是 HyperlinkedModelSerializer
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieStar
        fields = ('id','title','img','director','type','country','score','starring')


class StarringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Starring
        fields = ('id','actor','count','movie')
