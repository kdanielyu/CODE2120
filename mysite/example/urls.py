from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	path(r'example_get/<str:var_a>/<int:var_b>',  views.example_get),
	path(r'example_post/', views.example_post),
]