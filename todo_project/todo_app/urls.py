from django.contrib import admin
from . import views, path


urlpatterns = [
    path('', views.index),
    path('list', views.list),
    path('show', views.show),
    path('new', views.new),
    path('edit', views.edit),
]
