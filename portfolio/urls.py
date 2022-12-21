from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', cache_page(60)(WomenHome.as_view()), name='home'), if we want o cache defined page
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('portfolio/', MyPortfolio.as_view(), name='portfolio'),
]
