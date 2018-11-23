"""quotes_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from quotes_project.views import IndexView, CategoryView, CategoriesList, AuthorsList, AuthorDetails

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^categories/(?P<category>[-\w]+)/$', CategoryView.as_view(), name="category"),
    url(r'^categories/$', CategoriesList.as_view(), name="categories"),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetails.as_view(), name='author'),
    url(r'^authors/$', AuthorsList.as_view(), name="authors"),
]
