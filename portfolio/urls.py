from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60)(home), name='home'), #if we want o cache defined page
    # path('', home, name='home'),
    path('about/', cache_page(60)(About.as_view()), name='about'),
    path('portfolio/', MyPortfolio.as_view(), name='portfolio'),
    path('portfolio/<slug:project_slug>', ShowProject.as_view(), name='project'),
]
