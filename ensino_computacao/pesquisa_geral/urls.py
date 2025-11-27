from django.urls import path, include
from . import views

urlpatterns = [
		path('', views.pesquisa, name='pesquisa_geral')

]