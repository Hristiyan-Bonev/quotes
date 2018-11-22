from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Category, Author, Quote
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
import random

class IndexView(TemplateView):

    template_name = 'index.html'
    # model = Authors

    def get_context_data(self, **kwargs):
        categories = Category.objects.all().order_by('category_id')[:5]
        quotes = Quote.objects.all().order_by('category_id')[:5]
        carousel_quotes = [random.choice(quotes) for _ in range(3)]
        carousel_images = [random.randint(1, 12) for _ in range(3)]
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        context['carousel_data'] = zip(carousel_quotes, carousel_images)
        return context


class CategoryView(ListView):
    model = Quote
    template_name = 'category_view.html'

    def get_queryset(self):
        self.category_quotes = Quote.objects.filter(category__category_id__contains=3)
        return self.category_quotes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category_quotes[:10]
        return context
