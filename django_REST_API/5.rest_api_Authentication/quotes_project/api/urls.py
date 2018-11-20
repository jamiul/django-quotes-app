from django.urls import path

from .views import QuoteAPIView
from .views import QuoteCategoryAPIView
from .views import QuoteAPIdetailView
from .views import QuoteAPInewView

urlpatterns = [
    path('', QuoteCategoryAPIView.as_view()),
    path('quotes/', QuoteAPIView.as_view()),
    path('quotes/<int:pk>/', QuoteAPIdetailView.as_view()),
    path('quotes/new', QuoteAPInewView.as_view()),
]