# Generated by Django 5.1.6 on 2025-03-04 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_biblioteca', '0002_rename_autori_libro_autore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='autore',
            new_name='autori',
        ),
    ]
