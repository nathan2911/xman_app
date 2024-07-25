from django.shortcuts import render
from projects import models
from ba.models import *
from projects.models import *
from rest_framework import generics
from .serializers import NationalFoodsSerializer, BaSerializer


class ListRecords(generics.ListCreateAPIView):
    queryset = NationalFoods.objects.all()
    serializer_class = NationalFoodsSerializer


class DetailRecords(generics.RetrieveUpdateDestroyAPIView):
    queryset = NationalFoods.objects.all()
    serializer_class = NationalFoodsSerializer


class FetchBA(generics.ListCreateAPIView):
    queryset = BrandAmbassador.objects.all()
    serializer_class = BaSerializer


class BaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandAmbassador.objects.all()
    serializer_class = BaSerializer
