
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from cadastro_aluno.api import router as router_cadastro_aluno 

api = NinjaAPI()

api.add_router("/cadastro_aluno/", router_cadastro_aluno)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls)
]
