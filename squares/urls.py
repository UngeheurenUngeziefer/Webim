from django.urls import path

from . import views

urlpatterns = [
    path('', views.squares, name='squares'),
    path('js_page.html/', views.jspage, name='js_page'),
]
