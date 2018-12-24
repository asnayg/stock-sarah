# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Cliente
from .models import Producto

class IndexView(generic.ListView):
    template_name = 'appstock/index.html'
    context_object_name = 'productos_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Producto.objects.order_by('-fecha_entrada')[:5]

class ClientesView(generic.ListView):
    template_name = 'appstock/clientes.html'
    context_object_name = 'clientes_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Cliente.objects.order_by('-ubicacion')[:5]

class DetailView(generic.DetailView):
    model = Producto
    template_name = 'appstock/detail.html'
