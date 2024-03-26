from django.urls import path
from AppBlogCocina import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About"),
    path('listaRecetas/', views.RecetaListView.as_view(), name="Lista"),
    path('crear', views.RecetaCreateView.as_view(), name='New'),
    path('detalle/<int:pk>/', views.RecetaDetalle.as_view(), name='Detail'),
    path('editar/<int:pk>/', views.RecetaUpdateView.as_view(), name='Edit'),
    path('borrar/<int:pk>/', views.RecetaDeleteView.as_view(), name='Delete'),


]