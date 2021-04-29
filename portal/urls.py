from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name="list"),
    # path('add/', views.addProject, name="add"),
    # path('base/', views.baseProject, name="base"),
    # path('update/<str:pk>/', views.updateProject, name="update"),
	# path('delete/<str:pk>/', views.deleteProject, name="delete"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)