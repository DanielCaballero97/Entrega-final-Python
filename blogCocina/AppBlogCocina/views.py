from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppBlogCocina.models import Receta , Image
from AppBlogCocina.forms import RecetaImagenFormulario
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.shortcuts import render
from users.models import Avatar
from django.contrib.auth.models import User




def inicio(request):
    try:
        avatares = Avatar.objects.get(user=request.user.id)
        imagen = avatares.imagen.url
    except:
        imagen=""

    return render(
        request,
        "AppBlogCocina/index.html",
        {"url": imagen}
    )

def about(request):
    return render(request, "AppBlogCocina/nosotros.html")



from django.contrib.auth.models import User

class RecetaListView(ListView):
    model = Receta
    template_name = "AppBlogCocina/receta_list.html"


class RecetaDetalle(LoginRequiredMixin, DetailView):
    model = Receta
    template_name = "AppBlogCocina/receta_detalle.html"
    


class RecetaCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    template_name = "AppBlogCocina/receta_form.html"
    success_url = "listaRecetas/"
    fields = [
            "nombre",
            "descripcion",
            "pasos_completos",
            "categoria",
        ]
    def form_valid(self, form):
            user =  User.objects.get(id=self.request.user.id)
            receta = Receta(user=user,
                             nombre=form.cleaned_data['nombre'],
                             descripcion=form.cleaned_data['descripcion'],
                             pasos_completos=form.cleaned_data['pasos_completos'],
                             categoria=form.cleaned_data['categoria'])
            receta.save()
            return render(self.request ,"AppBlogCocina/index.html")


    

class RecetaUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView ):
    model = Receta
    template_name = "AppBlogCocina/receta_edit.html"
    success_url = "/listaRecetas/"
    fields = [
            "nombre",
            "descripcion",
            "pasos_completos",
            "categoria",
        ]
    
    def test_func(self):
        my_obj=self.get_object()
        return my_obj.user_id == self.request.user.id



class RecetaDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Receta
    success_url = "/listaRecetas/"
    template_name = "AppBlogCocina/receta_confirm_delete.html"

    def test_func(self):
        my_obj=self.get_object()
        return my_obj.user_id == self.request.user.id
    


from django.contrib.auth.decorators import login_required

@login_required
def agregar_imagen(request):

    if request.method == "POST":
        mi_form = RecetaImagenFormulario(request.POST, request.FILES)
        
        if mi_form.is_valid():
            receta = Receta.objects.get(id=request.id)
            try:
                img = Image.objects.get(receta_id=receta)
            except Image.DoesNotExist:
                img = Image(receta_id=receta, image=mi_form.cleaned_data['imagen'])
            else:
                img.image = mi_form.cleaned_data['imagen']
            img.save()

            return render(request, "/listaRecetas/")
        
    else:
        mi_form = RecetaImagenFormulario()
    
    context_data = {"mi_form": mi_form}
    return render(request, "AppBlogCocina/agregar_img.html", context_data)







