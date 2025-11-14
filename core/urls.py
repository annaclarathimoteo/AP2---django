
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja import Redoc
from cadastro_aluno.api import router as router_cadastro_aluno 

api = NinjaAPI(
    version="1.0",
    title="API para o sistema de escola do Ibmec",
    description="Essa API serve para controlar as notas do aluno",
    docs=Redoc()
)

api.add_router("/cadastro_aluno/", router_cadastro_aluno)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls)
]
