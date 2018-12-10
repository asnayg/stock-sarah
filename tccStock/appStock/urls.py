
from django.urls import path

from . import views

app_name = 'appStock'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:prod_id>/', views.detail, name='detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('detalles/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
