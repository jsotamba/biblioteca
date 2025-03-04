import json
from django.core.management.base import BaseCommand

from apps.gestione_biblioteca.models import Autore, Editore, Libro


class Command(BaseCommand):
    help = 'Importa libri, autori e editori da un file JSON'

    def handle(self, *args, **kwargs):
        with open('db.json', 'r') as file:
            data = json.load(file)

            # Importa autori
            autori_dict = {}
            for autore_data in data['autori']:
                autore, _ = Autore.objects.get_or_create(
                    id=autore_data['id'],
                    defaults={
                        'nome': autore_data['nome'],
                        'cognome': autore_data['cognome']
                    }
                )
                autori_dict[autore_data['id']] = autore

            # Importa editori
            editori_dict = {}
            for editore_data in data['editori']:
                editore, _ = Editore.objects.get_or_create(
                    id=editore_data['id'],
                    defaults={
                        'ragione_sociale': editore_data['ragione sociale'],
                        'indirizzo': editore_data.get('indirizzo'),
                        'telefono': editore_data.get('telefono')
                    }
                )
                editori_dict[editore_data['id']] = editore

            # Importa libri
            for libro_data in data['libri']:
                libro = Libro.objects.create(
                    titolo=libro_data['titolo'],
                    editore=editori_dict[libro_data['editore']],
                    anno_edizione=libro_data.get('anno edizione')
                )
                libro.autori.set([autori_dict[autore_id] for autore_id in [libro_data['autore']]])

        self.stdout.write(self.style.SUCCESS('Dati importati con successo!'))


if __name__ == '__main__':
    Command().execute()