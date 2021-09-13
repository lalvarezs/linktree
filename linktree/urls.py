from django.urls import path
from django.urls.conf import include
from linktree import views
urlpatterns = [
    path('', views.home_page_view)
]
