from django import forms
from AppBlogCocina.models import Receta , Image


class CargaReceta(forms.ModelForm):
    class Meta:
        model = Receta

        fields = [
            "nombre",
            "descripcion",
            "pasos_completos",
            "categoria",
        ]

class RecetaImagenFormulario(forms.ModelForm):
    class  Meta:
        model = Image
        fields = ["image"]

    