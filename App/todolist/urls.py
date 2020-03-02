from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('deletar/<list_id>', views.delete, name='delete'),
    path('riscar/<list_id>', views.cross_off, name='cross_off'),
    path('desfazer/<list_id>', views.uncross, name='uncross'),
    path('editar/<list_id>', views.edit, name='edit'),
]
