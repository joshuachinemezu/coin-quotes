from django.urls import include, path
from quotes import views


app_name = 'quotes'


urlpatterns = [
    path('quotes/', views.QuoteView.as_view()),
]
