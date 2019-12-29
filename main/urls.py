from django.urls import path
from .views import home,SearchView


urlpatterns = [
    path('', home, name='home'),
    path('search/', SearchView.as_view(), name='search')
]