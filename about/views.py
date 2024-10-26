from django.shortcuts import render
from .models import AboutMV
from .models import GalleryMV
from .models import TermsConditions

# Create your views here.
def mateo_vergara(request):
    # Esta vista le muestra al usuario la tabla de elementos de protección personal
    about_items = AboutMV.objects.order_by('id')
    gallery = GalleryMV.objects.order_by('id')
    return render(request, 'about/mateo_vergara.html',{'abouts':about_items,'about_gallery':gallery})

def terms_and_conditions(request):
    # Esta vista le muestra al usuario los terminos y condiciones de uso de la aplicación
    term_items = TermsConditions.objects.order_by('id')
    return render(request, 'about/terms_and_conditions.html',{'terms':term_items})
