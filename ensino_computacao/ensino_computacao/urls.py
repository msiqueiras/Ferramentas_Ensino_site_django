from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ferramentas_ensino/', include('pesquisa_geral.urls'))
]
