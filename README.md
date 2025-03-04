# 📚 Biblioteca API

Un progetto Django REST Framework per la gestione di una biblioteca, con funzionalità CRUD per libri, autori ed editori.

---

## 🛠 Installazione e Avvio del Progetto

# Creare e attivare un ambiente virtuale
python -m venv venv
source venv/bin/activate  # Su Mac/Linux
venv\Scripts\activate  # Su Windows

# Installare le dipendenze
pip install -r requirements.txt

# Configurare il database
python manage.py migrate
Se si desidera utilizzare un database diverso da SQLite, modificare DATABASES in settings.py e poi applicare nuovamente le migrazioni

# Importare i dati dal file db.json
python manage.py importa_libri

# Creare un superutente Django Admin
python manage.py createsuperuser

# Avviare il server di sviluppo
python manage.py runserver


## 📌 Editori

### 🔹 Endpoints disponibili

| Metodo | Endpoint                     | Descrizione                              |
|--------|------------------------------|------------------------------------------|
| GET    | `/`                          | Ottiene la lista dei libri salvati a db. |
| POST   | `/api/libri/`                | Inserisci un nuovo libro                 |
| GEST   | `/api/libri/?page_size=10`   | Lista dei libri paginata, di default 5.  |

### ✅ Esempio di richiesta **POST** /api/libri/
```json
{
  "titolo": "Nuovo Libro Django",
  "autori": [1, 2],
  "editore": 1,
  "anno_edizione": 2024
}