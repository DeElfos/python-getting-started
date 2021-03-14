from django.urls import path, include
from django.conf.urls import url, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    #url(r'^$', hello.views.index , name='index'),
    #url(r'^reque/$', hello.views.requ, name='search'),
    #path("", hello.views.index, name="index"),
    #path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("reque/", hello.views.requ, name="machine" )
]
