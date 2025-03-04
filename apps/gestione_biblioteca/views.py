from django.shortcuts import render
from rest_framework import viewsets, pagination, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.gestione_biblioteca.models import Libro, Autore, Editore
from apps.gestione_biblioteca.serializers import LibroSerializer


# Create your views here.
# per paginazione personalizzata
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('anno_edizione')
    serializer_class = LibroSerializer
    pagination_class = StandardResultsSetPagination  # paginazione personalizzata

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "Nessun libro disponibile."})
        return super().list(request, *args, **kwargs)


class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


def elenco_libri(request):
    libri = Libro.objects.all().order_by('anno_edizione')
    return render(request, 'elenco_libri.html', {'libri': libri})


@api_view(['POST'])
def create_from_json(request):
    data = request.data
    autori_data = data.get("autori", [])
    editori_data = data.get("editori", [])
    libri_data = data.get("libri", [])

    autori = {}
    editori = {}

    for autore in autori_data:
        obj, _ = Autore.objects.get_or_create(id=autore['id'], defaults=autore)
        autori[autore['id']] = obj

    for editore in editori_data:
        obj, _ = Editore.objects.get_or_create(id=editore['id'], defaults=editore)
        editori[editore['id']] = obj

    for libro in libri_data:
        nuovo_libro = Libro.objects.create(
            titolo=libro['titolo'],
            editore=editori[libro['editore']],
            anno_edizione=libro.get('anno edizione')
        )

        # trasformo autore in una lista se non lo è.
        autore_id = libro['autore']
        if autore_id:
            autore_obj = autori[autore_id]
            if autore_obj:
                nuovo_libro.autori.add(autore_obj)

    return Response({"message": "Dati importati con successo!"})
