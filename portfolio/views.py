from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .forms import *
from .models import *
from .utils import *

menu = [{'title': 'Main', 'url_name': 'home'},
        {'title': 'Who am I?', 'url_name': 'about'},
        {'title': 'My projects', 'url_name': 'portfolio'},
        ]


def home(request):
    context = {'title': 'Main Page',
               'selected': 'Main',
               'menu': menu
               }
    return render(request, 'portfolio/home.html', context=context)


def about(request):
    context = {'title': 'About Me',
               'selected': 'Who am I?',
               'menu': menu
               }
    return render(request, 'portfolio/about.html', context=context)


class MyPortfolio(ListView):
    model = MyProject
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyPortfolio, self).get_context_data(**kwargs)
        context['menu'] = menu
        context['selected'] = context['title'] = 'My projects'
        return context


class ShowProject(DetailView):
    model = MyProject
    template_name = 'portfolio/oneproject.html'
    slug_url_kwarg = 'project_slug'
    context_object_name = 'p'

    def get_context_data(self, **kwargs):
        context = super(ShowProject, self).get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['p']
        context['selected'] = 'My projects'

        context['images'] = ProjectImage.objects.filter(project_id=context['object'].id)
        return context
