from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<username>/<int:film_id>/comment/', views.add_comment, name='add_comment'),
]