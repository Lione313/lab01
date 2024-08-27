from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('calcular/<int:pago>/<int:num_horas>/', views.calcular, name='calcular'),


]
