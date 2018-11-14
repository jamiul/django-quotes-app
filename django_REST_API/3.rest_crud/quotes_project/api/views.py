from rest_framework import generics
from django.shortcuts import render

from quotes.models import Quote
from quotes.models import QuoteCategory

from .serializers import QuoteSerializer
from .serializers import QuoteCategorySerializer

class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer 

class QuoteAPIdetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteAPInewView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')[:1]
    #latest quote
    serializer_class = QuoteSerializer  


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class  = QuoteCategorySerializer

