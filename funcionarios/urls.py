from django.urls import path
from .views import (
    FuncionarioListView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView
)

app_name = 'funcionarios'

urlpatterns = [
    path('', FuncionarioListView.as_view(), name='list'),
    path('novo/', FuncionarioCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', FuncionarioUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', FuncionarioDeleteView.as_view(), name='delete'),
] 