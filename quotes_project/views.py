from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Author, Quote
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
import random
import re

class IndexView(TemplateView):

    template_name = 'index.html'
    # model = Authors

    def get_context_data(self, **kwargs):
        categories = Category.objects.all().order_by('category_id')[:15]
        quotes = Quote.objects.all().order_by('category_id')[:15]
        carousel_quotes = [random.choice(quotes) for _ in range(3)]
        carousel_images = [random.randint(1, 12) for _ in range(3)]
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        context['carousel_data'] = zip(carousel_quotes, carousel_images)
        return context


class CategoryView(ListView):
    model = Category
    template_name = 'category_view.html'

    def get_queryset(self):
        self.category_id = Category.objects.filter(category=self.kwargs['category']).values('category_id')
        self.category_quotes = Quote.objects.filter(category__category_id__contains=self.category_id)
        self.category = Category.objects.filter(category=self.kwargs['category'])
        return self.category_quotes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = self.category_quotes[:24]
        context['category'] = self.category
        context['image_no'] = [random.randint(1,10) for _ in range(len(context['quotes']))]
        return context


class CategoriesList(ListView):
    model=Category
    template_name='category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories[:1204]
        context['categories_count'] = len(context['categories'])
        return context

class AuthorsList(ListView):
    model=Author
    template_name = 'authors_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.all()
        char_list = list(set([x.author[0] for x in authors]))
        # Set of alphanumeric chars only
        unique_chars = set([char.lower() for char in char_list if ord(char) < 128])
        # Get only alphabet letters
        unique_chars = sorted([char for char in unique_chars if char.isalpha()])
        sorted_authors={}

        for char in unique_chars:
            # Create dictionary with first letter as key and corresponding
            # authors with first letter matching as values
            sorted_authors[char] = sorted([(x.author.strip(), x.author_id)  \
                                           for x in authors \
                                           if x.author[0].lower() == char \
                                           and len(x.author) < 15])

        # import ipdb; ipdb.set_trace()
        context['authors'] = sorted_authors
        context['authors_count'] = len(authors)
        return context


class AuthorDetails(DetailView):
    model=Author
    template_name = 'author_details.html'
    slug_field = 'author_id'

    # def get_queryset(self):
    #     import ipdb; ipdb.set_trace()
    #     return self.author_quotes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.author = Author.objects.filter(author_id=self.kwargs['pk'])
        self.author_quotes = Quote.objects.filter(author__author_id__contains=self.kwargs['pk'])
        context['author'] = self.author
        context['author_quotes'] = self.author_quotes
        return context
