from rest_framework import serializers
from apps.gestione_biblioteca.models import Libro, Autore, Editore


class AutoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autore
        fields = '__all__'


class EditoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editore
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    autori = serializers.PrimaryKeyRelatedField(many=True, queryset=Autore.objects.all())
    editore = serializers.PrimaryKeyRelatedField(queryset=Editore.objects.all())

    class Meta:
        model = Libro
        fields = '__all__'
