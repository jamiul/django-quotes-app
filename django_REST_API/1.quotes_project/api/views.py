from rest_framework import generics
from django.shortcuts import render

from quotes.models import Quote
from quotes.models import QuoteCategory

from .serializers import QuoteSerializer
from .serializers import QuoteCategorySerializer

class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteCategorySerializer

class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class  = QuoteCategorySerializer   


