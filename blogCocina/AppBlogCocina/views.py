from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppBlogCocina.models import Receta 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class RecetaListView(LoginRequiredMixin, ListView):
    model = Receta
    template_name = "AppBlogCocina/receta_list.html"


class RecetaDetalle(DetailView):
    model = Receta
    template_name = "AppBlogCocina/receta_detalle.html"


class RecetaCreateView(CreateView):
    model = Receta
    template_name = "AppBlogCocina/receta_form.html"
    success_url = reverse_lazy("List")
    fields = ["nombre", "camada"]


class RecetaUpdateView(UpdateView):
    model = Receta
    template_name = "AppBlogCocina/receta_edit.html"
    success_url = "/AppBlogCocina/clases/lista/"
    fields = ["nombre", "camada"]


class RecetaDeleteView(DeleteView):
    model = Receta
    success_url = reverse_lazy("List")
    template_name = "AppBlogCocina/receta_confirm_delete.html"